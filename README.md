OpenCV Fast Image Processing (YOLOv8)

Process live camera images using OpenCV and YOLOv8 with Python.
This project performs real-time object detection from your webcam and displays the results instantly on screen.

Overview

This project demonstrates how to combine:

OpenCV for camera access and image processing

YOLOv8 for AI powered object detection

Python for rapid development

The system captures frames from the webcam, runs them through a YOLOv8 neural network, and displays detected objects with bounding boxes and FPS information.

Features

Real-time object detection

Webcam processing with OpenCV

YOLOv8 neural network integration

FPS monitoring

Fullscreen display mode

Simple automatic setup

Lightweight YOLOv8 model support

Project Structure
project-folder
│
├── setup.py
├── start.py
├── yolov8n.pt
├── requirements.txt
└── README.md
Installation

Clone the repository:

git clone https://github.com/kzlparasonic/OpenCV-Fast-Image-Processing

Enter the project directory:

cd OpenCV-Fast-Image-Processing

Run the setup file:

python setup.py

The setup script will:

Install required Python packages

Prepare the environment

Launch the application automatically

Usage

Once the program starts:

Your webcam will activate

YOLOv8 will analyze each frame

Detected objects will appear with bounding boxes

FPS will be displayed in the corner

Press Q to exit the program.

Requirements

Python 3.9+

Libraries used:

OpenCV

Ultralytics YOLOv8

PyTorch

NumPy

These dependencies are automatically installed using requirements.txt.

Performance Tips

For the best performance:

Use a GPU with CUDA support

Lower the camera resolution if needed

Use smaller YOLO models such as yolov8n

Future Improvements

Possible upgrades for this project:

Object tracking

Distance estimation

AI danger detection system

Augmented reality overlays

Multi-camera support

Edge device deployment (Jetson / Raspberry Pi)

Author

Developed by StarkDev

Company Website
https://starkdev.com.tr

License

MIT License

This project is open source and available for educational and research purposes.
