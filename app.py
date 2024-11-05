from flask import Flask, render_template, request, jsonify
from utils.image_processing import preprocess_image, load_model, predict_pneumonia
import logging
from google.cloud import storage
import os

# Initialize storage client
storage_client = storage.Client()
bucket_name = 'pneumonia-detector-uploads'
bucket = storage_client.bucket(bucket_name)

def upload_to_gcs(file):
    blob = bucket.blob(file.filename)
    blob.upload_from_string(
        file.read(),
        content_type=file.content_type
    )
    return blob.public_url

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# Load your saved model
try:
    model = load_model('Models/pneumonia_model.h5')
except Exception as e:
    logging.error(f"Failed to load model: {e}")
    model = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        # Upload the file to Google Cloud Storage
        public_url = upload_to_gcs(file)

        # Read the file for processing
        file.seek(0)
        file_bytes = file.read()
        img_array = preprocess_image(file_bytes)
        probability = predict_pneumonia(model, img_array)
        
        if probability > 0.5:
            result = f"Probability of pneumonia: {probability:.2f}. The person may have pneumonia."
        else:
            result = f"Probability of pneumonia: {probability:.2f}. The person is likely free from pneumonia."
        
        return jsonify({'result': result, 'image_url': public_url})
    except Exception as e:
        logging.error(f"Error processing image: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=True)
