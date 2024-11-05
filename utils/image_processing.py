import tensorflow as tf
import numpy as np
from PIL import Image
import io
import logging

logging.basicConfig(level=logging.INFO)

def preprocess_image(image_data, target_size=(120, 120)):
    try:
        if isinstance(image_data, np.ndarray):
            # If input is already a numpy array
            img_array = image_data
        elif isinstance(image_data, (bytes, io.BytesIO)):
            # If input is bytes or BytesIO (from file upload)
            img = Image.open(io.BytesIO(image_data) if isinstance(image_data, bytes) else image_data)
            img = img.convert('RGB')  # Ensure image is in RGB format
            img = img.resize(target_size)
            img_array = np.array(img)
        else:
            raise ValueError("Unsupported image_data type")
        
        img_array = img_array / 255.0  # Normalize to [0, 1]
        img_array = np.expand_dims(img_array, axis=0)
        logging.info("Image preprocessed successfully.")
        return img_array
    except Exception as e:
        logging.error(f"Error in preprocessing image: {e}")
        raise

def load_model(model_path):
    try:
        model = tf.keras.models.load_model(model_path)
        logging.info("Model loaded successfully.")
        return model
    except Exception as e:
        logging.error(f"Error in loading model: {e}")
        raise

def predict_pneumonia(model, image_array):
    try:
        prediction = model.predict(image_array)
        probability = float(prediction[0][0])
        logging.info("Prediction made successfully.")
        return probability
    except Exception as e:
        logging.error(f"Error in making prediction: {e}")
        raise