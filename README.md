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

## Usage

Run the application:
cd application
python main.py

## Model Training

The model was trained using YOLOv8 on a custom drone dataset. See the model_training/ folder for the Colab notebook.

## Results
![Result_1_img](https://github.com/user-attachments/assets/c8fad08c-3ca1-4695-a612-ca586773b367)
![Result_2_img](https://github.com/user-attachments/assets/a79903a1-4a25-4161-bbc3-1c3e92f11fe7)
![Result_3_vid](https://github.com/user-attachments/assets/91529914-f4a6-4f92-8146-18d6b574789c)
