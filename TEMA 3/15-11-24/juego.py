import cv2
import mediapipe as mp
import random
import time
import speech_recognition as sr
import threading

# Inicializar cámara y configuración de mediapipe
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                       min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Constantes del juego
width, height = 800, 800
player_position_x = width // 20
player_position_y = height - 100
player_speed = 15
obstacle_speed = 5
coin_speed = 5
shield_speed = 8
special_item_speed = 8
score = 0
level = 1
lives = 3
obstacles = []
coins = []
shields = []
special_item = None
shield_active = False
shield_count = 0

# Cargar imágenes PNG
player_img = cv2.imread('player.png', cv2.IMREAD_UNCHANGED)
obstacle_img = cv2.imread('obstacle.png', cv2.IMREAD_UNCHANGED)
coin_img = cv2.imread('coin.png', cv2.IMREAD_UNCHANGED)
shield_img = cv2.imread('shield.png', cv2.IMREAD_UNCHANGED)
special_item_img = cv2.imread('special_item.png', cv2.IMREAD_UNCHANGED)

# Redimensionar imágenes
player_img = cv2.resize(player_img, (50, 50))
obstacle_img = cv2.resize(obstacle_img, (50, 50))
coin_img = cv2.resize(coin_img, (30, 30))
shield_img = cv2.resize(shield_img, (50, 50))
special_item_img = cv2.resize(special_item_img, (50, 50))

# Tiempo de inicio
start_time = time.time()

def overlay_image(background, overlay, x, y):
    """Superpone una imagen con canal alfa sobre otra en una posición (x, y)."""
    if overlay.shape[2] == 3:  # Convertir a BGRA si no tiene canal alfa
        overlay = cv2.cvtColor(overlay, cv2.COLOR_BGR2BGRA)
    h, w = overlay.shape[:2]
    if y + h > background.shape[0] or x + w > background.shape[1] or y < 0 or x < 0:
        return
    alpha_overlay = overlay[:, :, 3] / 255.0
    alpha_background = 1.0 - alpha_overlay
    for c in range(3):  # Para los canales de color
        background[y:y + h, x:x + w, c] = (alpha_overlay * overlay[:, :, c] +
                                           alpha_background * background[y:y + h, x + w, c])

def listen_for_shield_command():
    """Escucha un comando de voz para activar el escudo."""
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    global shield_active, shield_count
    while True:
        with mic as source:
            try:
                recognizer.adjust_for_ambient_noise(source)
                print("Escuchando... Di 'usar' para activar el escudo.")
                
                # Escuchar comando de voz
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio, language='es-ES').lower()
                
                # Activar escudo si el comando coincide
                if "usar" in command and shield_count > 0:
                    shield_active = True
                    shield_count -= 1
                    print("Escudo activado!")
            except sr.UnknownValueError:
                print("No se entendió el comando.")
            except sr.RequestError:
                print("Error en el servicio de reconocimiento de voz.")
            except sr.WaitTimeoutError:
                print("No se detectó ninguna palabra a tiempo.")

# Crear hilo para el reconocimiento de voz
thread = threading.Thread(target=listen_for_shield_command, daemon=True)
thread.start()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Redimensionar el cuadro y crear un fondo negro para la interfaz
    frame = cv2.resize(frame, (width, height))
    frame = cv2.flip(frame, 1)
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesar la imagen para detectar manos
    results = hands.process(image_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            index_finger_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * width)
            index_finger_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height)
            player_position_x = index_finger_x
            player_position_y = index_finger_y

    # Limitar posición del jugador
    player_position_x = max(0, min(width - 50, player_position_x))
    player_position_y = max(0, min(height - 50, player_position_y))

    # Generar obstáculos, monedas, escudos y objeto especial
    if random.randint(1, max(30 - level, 5)) == 1:
        obstacles.append([random.randint(0, width - 50), 0, random.choice([-1, 1])])
    if random.randint(1, 30) == 1:
        coins.append([random.randint(0, width - 30), 0])
    if random.randint(1, 200) == 1:
        shields.append([random.randint(0, width - 50), 0])
    if not special_item and random.randint(1, 250) == 1:
        special_item = [random.randint(0, width - 50), 0]

    # Dibujar obstáculos, monedas, escudos y objeto especial
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
        overlay_image(frame, obstacle_img, obstacle[0], obstacle[1])
    for coin in coins:
        coin[1] += coin_speed
        overlay_image(frame, coin_img, coin[0], coin[1])
    for shield in shields:
        shield[1] += shield_speed
        overlay_image(frame, shield_img, shield[0], shield[1])
    if special_item:
        special_item[1] += special_item_speed
        overlay_image(frame, special_item_img, special_item[0], special_item[1])

    # Detectar colisiones
    for obstacle in obstacles[:]:
        if (player_position_x < obstacle[0] + 50 and
                player_position_x + 50 > obstacle[0] and
                player_position_y < obstacle[1] + 50 and
                player_position_y + 50 > obstacle[1]):
            obstacles.remove(obstacle)
            if shield_active:
                shield_active = False  # Desactivar escudo tras absorber la colisión
                print("El escudo absorbió el impacto y se desactivó.")
            else:
                lives -= 1
                if lives == 0:
                    cv2.putText(frame, 'GAME OVER', (width // 2 - 100, height // 2),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
                    cv2.imshow('Recolecta monedas', frame)
                    cv2.waitKey(0)
                    cap.release()
                    cv2.destroyAllWindows()
                    exit()

    for coin in coins[:]:
        if (player_position_x < coin[0] + 30 and
                player_position_x + 50 > coin[0] and
                player_position_y < coin[1] + 30 and
                player_position_y + 50 > coin[1]):
            coins.remove(coin)
            score += 1
            if score % 5 == 0:
                level += 1
                obstacle_speed += 1
                coin_speed += 1

    for shield in shields[:]:
        if (player_position_x < shield[0] + 50 and
                player_position_x + 50 > shield[0] and
                player_position_y < shield[1] + 50 and
                player_position_y + 50 > shield[1]):
            shields.remove(shield)
            shield_count += 1

    if special_item and (player_position_x < special_item[0] + 50 and
                         player_position_x + 50 > special_item[0] and
                         player_position_y < special_item[1] + 50 and
                         player_position_y + 50 > special_item[1]):
        special_item = None
        lives += 1

    # Eliminar objetos fuera de pantalla
    obstacles = [obstacle for obstacle in obstacles if obstacle[1] < height]
    coins = [coin for coin in coins if coin[1] < height]
    shields = [shield for shield in shields if shield[1] < height]

    # Dibujar jugador y escudo
    overlay_image(frame, player_img, player_position_x, player_position_y)
    if shield_active:
        overlay_image(frame, shield_img, player_position_x, player_position_y)
        cv2.putText(frame, 'Escudo Activo', (width - 250, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Mostrar estadísticas
    elapsed_time = int(time.time() - start_time)
    cv2.putText(frame, f'Tiempo: {elapsed_time}s', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f'Puntaje: {score}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f'Nivel: {level}', (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f'Vidas: {lives}', (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f'Escudos: {shield_count}', (10, 190), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Mostrar ventana del juego
    cv2.imshow('Recolecta monedas', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
