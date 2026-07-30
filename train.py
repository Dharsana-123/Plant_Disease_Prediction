import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
train_dir = "dataset/train"
val_dir = "dataset/val"
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode="categorical"
)
val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode="categorical"
)
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation="relu", input_shape=(224,224,3)),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Conv2D(64, (3,3), activation="relu"),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(128, activation="relu"),

    tf.keras.layers.Dense(train_generator.num_classes, activation="softmax")
])
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=10
)
model.save("plant_disease_model.h5")
print(train_generator.class_indices)

with open("classes.txt", "w") as f:
    for class_name in train_generator.class_indices:
        f.write(class_name + "\n")
print("Model saved successfully!")
