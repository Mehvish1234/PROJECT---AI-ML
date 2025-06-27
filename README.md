# Face Mask Detection System
FULL WORKING VIDEO OF THE MODEL :
[FULL VIDEO LINK ](https://drive.google.com/file/d/1ud21xv2-D9jPkTkRBPh0sZhbcRNR5VbP/view?usp=drive_link)

A real-time face mask detection system built with Flask and TensorFlow. This web application provides two methods for detecting whether someone is wearing a face mask: real-time webcam detection and image upload analysis.

![Face Mask Detection](https://img.shields.io/badge/Face%20Mask-Detection-brightgreen)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)

## Features

### 1. Multiple Detection Methods
- **Real-time Webcam Detection**: Use your device's camera for instant mask detection
- **Image Upload Analysis**: Upload images from your device for mask detection

### 2. User-Friendly Interface
- Modern, responsive design
- Intuitive navigation
- Real-time feedback
- Loading indicators
- Image preview before analysis

### 3. Alert System
- Visual indicators for mask detection status
- Audio alerts when no mask is detected
- Color-coded results (green for mask, red for no mask)
- Animated feedback

## Prerequisites

- Python 3.7 or higher
- Webcam (for real-time detection)
- Modern web browser (Chrome, Firefox, Safari, Edge)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd face-mask-detection
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install flask tensorflow pillow numpy
```

## Project Structure

```
face-mask-detection/
│
├── app.py                 # Flask application
├── face_mask_model_updated.h5    # Trained model
│
├── templates/
│   ├── index.html        # Landing page
│   ├── webcam.html       # Webcam detection page
│   └── upload.html       # Image upload page
│
└── README.md             # Project documentation
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Choose your preferred detection method:
   - Click "Launch Camera" for real-time webcam detection
   - Click "Upload Image" to analyze saved images

### Using Webcam Detection

1. Allow camera access when prompted
2. Position your face in the camera view
3. Click "Capture & Check" to analyze
4. View results with visual and audio feedback

### Using Image Upload

1. Click the upload area or drag and drop an image
2. Preview your image
3. Click "Check Image" to analyze
4. View results with visual and audio feedback

## Model Information

The system uses a pre-trained deep learning model (`face_mask_model_updated.h5`) to detect the presence of face masks. The model:
- Accepts 224x224 RGB images as input
- Provides binary classification (mask/no mask)
- Returns confidence scores for predictions


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- TensorFlow team for the deep learning framework
- Flask team for the web framework
- Contributors to the face mask detection dataset 
