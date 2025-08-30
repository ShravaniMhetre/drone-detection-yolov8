# Drone Detection using YOLOv8

A real-time drone detection system using YOLOv8 with a graphical user interface.

## Features

- Image-based drone detection
- Real-time webcam detection
- Video file processing
- FPS counter for performance monitoring
- Modern GUI with ttkbootstrap

## Installation

1. Clone the repository:

git clone https://github.com/ShravaniMhetre/drone-detection-yolov8.git
cd drone-detection-yolov8

2. Install dependencies:

cd application
pip install -r requirements.txt

3. Download the trained model:

Place your best.pt file in the application/models/ folder
Or train your own model using the Colab notebook

Usage

Run the application:
cd application
python main.py

Model Training

The model was trained using YOLOv8 on a custom drone dataset. See the model_training/ folder for the Colab notebook.
