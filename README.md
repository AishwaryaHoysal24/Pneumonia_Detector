# 🩺 Pneumonia Detector

Welcome to the **Pneumonia Detector** project! This Flask-based web application leverages a Convolutional Neural Network (CNN) to detect pneumonia from chest X-ray images. Whether you're a healthcare professional or a curious developer, this tool provides a seamless interface to upload X-rays and receive predictions in real-time.

## 🌟 Features

- **Image Upload**: Easily upload chest X-ray images in PNG or JPEG format.
- **AI-Powered Detection**: Uses a pre-trained CNN model to analyze X-rays and predict the probability of pneumonia.
- **Interactive Chatbot**: Get instant answers to pneumonia-related questions through an integrated chatbot.
- **User-Friendly Interface**: Simple and intuitive web interface designed for ease of use.

## 🚀 Quick Start Guide

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone <https://github.com/yourusername/pneumonia-detector.git>
cd pneumonia-detector

```

### 2. Set Up Your Environment

To ensure all dependencies are managed, set up a virtual environment:

```bash
python -m venv venv

```

Activate the environment:

- **Windows**: `venv\\Scripts\\activate`
- **macOS/Linux**: `source venv/bin/activate`

### 3. Install Dependencies

With the virtual environment activated, install all required packages:

```bash
pip install -r requirements.txt

```

### 4. Run the Application

Start the Flask server to launch the application:

```bash
python app.py

```

### 5. Access the Web Interface

Open your web browser
Here, you can upload chest X-ray images and receive predictions.

### 6. Upload and Detect

- **Upload**: Select a chest X-ray image using the "Choose File" button.
- **Detect**: Click "Submit" to see the probability of pneumonia.
- **Chat**: Ask the integrated chatbot any questions related to pneumonia.

### 7. Terminate the Application

Once you're done, stop the Flask server with `Ctrl+C` in the terminal. Deactivate your virtual environment by typing `deactivate`.

## 🔧 Troubleshooting

- **Model Loading Issues**: Ensure the `pneumonia_model.h5` file is located in the `Models` folder.
- **Dependencies**: Double-check that all packages in `requirements.txt` are installed.
- **Server Not Running?**: Verify that your terminal is in the project root and the virtual environment is activated.

## 🎯 Future Enhancements

- **Improved Model Accuracy**: Further training to increase prediction accuracy.
- **Multi-Image Support**: Allow batch processing of multiple X-rays.
- **Enhanced Chatbot**: Expand the chatbot's knowledge base for more comprehensive responses.

## 🤝 Contributing

Feel free to fork the repository, submit pull requests, or open issues for discussion.

---

Happy coding! If you find this project useful, give it a ⭐️ on GitHub.

---
