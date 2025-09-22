# Importing libraries
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from google.colab import drive
# Step 1: Mount Google Drive to access the dataset
from google.colab import drive
drive.mount('/content/drive')

# Set the paths to your dataset folders in Google Drive
genuine_dir = '/content/drive/My Drive/SIGN/real/'
forged_dir = '/content/drive/My Drive/SIGN/forged/'

# ----------------------
# Image Preprocessing
# ----------------------

def preprocess_image(image_path, target_size=(128, 128)):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img_resized = cv2.resize(img, target_size)
    img_normalized = img_resized / 255.0
    return img_normalized

def load_and_preprocess_images(image_paths, target_size=(128, 128)):
    return np.array([preprocess_image(path, target_size) for path in image_paths])

# ----------------------
# Data Augmentation
# ----------------------

def create_data_generator():
    return ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=False,
        fill_mode='nearest'
    )

# ----------------------
# CNN Model
# ----------------------

def create_cnn_model(input_shape=(128, 128, 1)):
    inputs = Input(shape=input_shape)
    
    x = Conv2D(32, (3, 3), activation='relu')(inputs)
    x = MaxPooling2D((2, 2))(x)
    x = Conv2D(64, (3, 3), activation='relu')(x)
    x = MaxPooling2D((2, 2))(x)
    x = Conv2D(64, (3, 3), activation='relu')(x)
    x = MaxPooling2D((2, 2))(x)
    
    x = Flatten()(x)
    x = Dense(64, activation='relu')(x)
    x = Dropout(0.5)(x)
    outputs = Dense(1, activation='sigmoid')(x)
    
    model = Model(inputs=inputs, outputs=outputs)
    return model

# ----------------------
# Model Training
# ----------------------

def train_model(train_data, train_labels, val_data, val_labels, epochs=50, batch_size=32):
    model = create_cnn_model()
    model.compile(optimizer=Adam(learning_rate=0.001),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    
    history = model.fit(train_data, train_labels,
                        validation_data=(val_data, val_labels),
                        epochs=epochs,
                        batch_size=batch_size)
    
    return model, history

# ----------------------
# Data Loading
# ----------------------

def load_data(genuine_dir, forged_dir):
    genuine_paths = [os.path.join(genuine_dir, f) for f in os.listdir(genuine_dir)]
    forged_paths = [os.path.join(forged_dir, f) for f in os.listdir(forged_dir)]
    
    genuine_images = load_and_preprocess_images(genuine_paths)
    forged_images = load_and_preprocess_images(forged_paths)
    
    X = np.concatenate([genuine_images, forged_images])
    y = np.concatenate([np.ones(len(genuine_images)), np.zeros(len(forged_images))])
    
    # Add a channel dimension for grayscale images
    X = X[..., np.newaxis]
    
    return X, y

# ----------------------
# Model Evaluation
# ----------------------

def evaluate_model(model, test_data, test_labels):
    predictions = model.predict(test_data)
    predictions_binary = (predictions > 0.5).astype(int)
    
    cm = confusion_matrix(test_labels, predictions_binary)
    cr = classification_report(test_labels, predictions_binary)
    
    print("Confusion Matrix:")
    print(cm)
    print("\nClassification Report:")
    print(cr)
    
    return cm, cr

def plot_training_history(history):
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Model Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Model Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# ----------------------
# Main Execution
# ----------------------

def main():
    # Load and preprocess data
    X, y = load_data(genuine_dir, forged_dir)
    
    # Split data into train, validation, and test sets
    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.2, random_state=42)
    
    # Train model
    model, history = train_model(X_train, y_train, X_val, y_val)
    
    # Evaluate model
    cm, cr = evaluate_model(model, X_test, y_test)
    
    # Plot training history
    plot_training_history(history)

# Run the main function
if __name__ == "__main__":
    main()
