import cv2
import mediapipe as mp
import random
import time

# Inicializar cámara y configuración de mediapipe
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                       min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Constantes del juego
width, height = 800, 800
player_position_x = width // 2
player_position_y = height - 50
player_speed = 15
obstacle_speed = 10
score = 0
obstacles = []
smoothing_factor = 1


start_time = time.time()

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

    # Detectar gestos de la mano
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Coordenadas de los dedos índice y pulgar
            index_finger_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * width
            thumb_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * width

            
            # Detectar el gesto para mover el jugador
            if index_finger_x < thumb_x:
                # Gesto "izquierda" - mover jugador a la izquierda
                player_position_x -= player_speed  * smoothing_factor
            elif index_finger_x > thumb_x:
                # Gesto "derecha" - mover jugador a la derecha
                player_position_x += player_speed * smoothing_factor

    # Limitar el movimiento del jugador a la pantalla
    player_position_x = max(0, min(width, player_position_x))

    # Agregar nuevos obstáculos
    if random.randint(1, 20) == 1:
        obstacle_x = random.randint(0, width)
        obstacles.append([obstacle_x, 0])

    # Dibujar y mover obstáculos
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed  # Mover obstáculo hacia abajo
        cv2.rectangle(frame, (obstacle[0], obstacle[1]), (obstacle[0] + 50, obstacle[1] + 50), (0, 0, 255), -1)

    # Detectar colisiones
    for obstacle in obstacles:
        if (player_position_x < obstacle[0] + 50 and
            player_position_x + 50 > obstacle[0] and
            player_position_y < obstacle[1] + 50 and
            player_position_y + 50 > obstacle[1]):
            # Si colisiona, termina el juego
            cv2.putText(frame, 'GAME OVER', (width // 2 - 100, height // 2), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
            cv2.imshow('Esquiva los obstáculos', frame)
            cv2.waitKey(0)
            cap.release()
            cv2.destroyAllWindows()
            exit()

    # Eliminar obstáculos fuera de la pantalla
    obstacles = [obstacle for obstacle in obstacles if obstacle[1] < height]

    # Dibujar el jugador
    cv2.rectangle(frame, (player_position_x, player_position_y), (player_position_x + 50, player_position_y + 50), (255, 255, 0), -1)

    # Calcular y mostrar puntaje
    elapsed_time = int(time.time() - start_time)
    score = elapsed_time
    cv2.putText(frame, f'Tiempo: {elapsed_time}s', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f'Puntaje: {score}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Mostrar la ventana del juego
    cv2.imshow('Esquiva los obstáculos', frame)

    # Salir si el usuario presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
