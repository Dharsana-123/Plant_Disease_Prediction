import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the trained model
model = load_model("plant_disease_model.h5")

# Load class names
with open("classes.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

print("Model loaded successfully!")

# Image path
img_path = input("Enter image path: ")

# Load and preprocess image
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

# Predict
prediction = model.predict(img_array)
predicted_class = class_names[np.argmax(prediction)]

print("Predicted Disease:", predicted_class)