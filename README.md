# Hand-Gesture-LED-Control-RaspberryPi
This project controls LEDs connected to a Raspberry Pi using hand gestures detected from a laptop camera. 
Computer vision is used to detect the number of fingers, and the system sends commands to the Raspberry Pi through WiFi to turn ON the corresponding LED.

Laptop Camera → OpenCV → MediaPipe Hand Detection → Finger Counting → HTTP Request → Raspberry Pi Flask Server → GPIO → LED

## Hardware Required
- Raspberry Pi 3/4/5
- LEDs (5)
- 220Ω Resistors
- Breadboard
- Jumper Wires
- Laptop with Camera

## Software Required
- Python
- OpenCV
- MediaPipe
- Flask

## Installation

Install libraries (laptop):
pip install opencv-python mediapipe requests

On Raspberry Pi
sudo apt install python3-flask

## Run the Project

Step 1: Start Flask server on Raspberry Pi
python3 led_server.py
Step 2: Run gesture detection on laptop
python gesture_led.py

## Gesture Mapping

1 Finger → LED1 ON  
2 Fingers → LED2 ON  
3 Fingers → LED3 ON  
4 Fingers → LED4 ON  
5 Fingers → LED5 ON

## Applications

- Touchless control systems
- Smart home automation
- IoT gesture interfaces

## Author

Darshan N  
Electronics and Communication Engineering
darshan72111@gmail.com
