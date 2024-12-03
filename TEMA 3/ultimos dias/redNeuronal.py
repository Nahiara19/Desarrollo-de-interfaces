import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# Cargar el modelo entrenado
model = tf.keras.models.load_model('ruta_a_tu_modelo/model.h5')

# Cargar y preprocesar la imagen
def prepare_image(image_path):
    # Cargar la imagen
    image = Image.open(image_path)
    
    # Redimensionar la imagen a 224x224 (dimensiones esperadas por el modelo)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    
    # Convertir la imagen en una matriz numpy y normalizar los valores a [0, 1]
    image_array = np.asarray(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = image_array / 255.0
    
    return image_array

# Función para hacer predicciones
def predict(image_path):
    image_array = prepare_image(image_path)
    
    # Hacer la predicción
    prediction = model.predict(image_array)
    
    # Obtener la clase con la mayor probabilidad
    predicted_class = np.argmax(prediction, axis=1)
    
    return predicted_class

# Ejemplo de uso
image_path = 'ruta_a_tu_imagen/image.jpg'
result = predict(image_path)
print(f"Predicción: {result}")
