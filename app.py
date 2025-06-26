from flask import Flask, render_template, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import io
import os

app = Flask(__name__)
model = load_model('face_mask_model_updated.h5', compile=False)  # Or your latest model

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webcam')
def webcam():
    return render_template('webcam.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'result': 'No image uploaded'}), 400

    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')
    image = image.resize((224, 224))  # Match model input
    img_array = np.array(image) / 255.0
    img_array = np.reshape(img_array, (1, 224, 224, 3))

    prediction = model.predict(img_array)
    label = "✅ Mask Detected" if prediction[0][0] < 0.5 else "❌ No Mask! Please Wear One"

    return jsonify({'result': label})

if __name__ == '__main__':
    app.run(debug=True)
