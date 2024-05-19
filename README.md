ASL Robotic Hand.
Overview
The ASL Robotic Hand project is an innovative solution designed to interpret and communicate American Sign Language through a robotic hand. It employs a multi-mode approach to capture and process human gestures and convert them into meaningful robotic hand movements and corresponding language displays. The project encompasses three primary modes of operation: Slider Mode, Camera Mode, and Voice Mode. It incorporates a network of embedded systems using ATmega32, Arduino Uno, and Bluetooth communication to facilitate wireless interaction and control.

1-Slider Mode: In this mode, 5 Slider POTs or flexible sensors are connected to an ATmega32, which converts the analog signals to digital data using an Analog-to-Digital Converter (ADC). The ATmega32 sends this data wirelessly via a Bluetooth module (HC05) to the Arduino Uno, which controls 5 servos responsible for manipulating the robotic hand's fingers.
2-Camera Mode: Utilizing OpenCV and Mediapipe libraries, this mode processes video input from a webcam to recognize hand gestures. This additional functionality enhances the flexibility of the robotic hand, allowing it to respond to visual cues and adapt to different scenarios.
3-Voice Mode: Through the Speech Recognition library, this mode allows voice-based interaction. Users can issue speech commands that the system translates into corresponding robotic hand gestures, providing an intuitive and flexible communication mechanism.
Project Nodes
The project is structured into three interconnected nodes, each with specific responsibilities:

ATmega32 Node (Master Node): This node connects to 5 Slider POTs or flexible sensors, capturing analog data from the sliders to determine the desired positions of the robotic hand's fingers. It also features a Bluetooth module (HC05) to communicate with the Arduino Node wirelessly.
Arduino Uno Node (Slave Node): The Arduino Uno acts as a shared slave node between the master nodes. It is connected to 5 servo motors that control each finger's movement, an LCD display, and a Bluetooth module (HC05). Upon receiving sensor data from the ATmega32, it performs two critical functions:
Servo Motor Control: Adjusts the servo motors based on the received sensor data, correlating to specific finger movements.
Language Display: Displays language words on an LCD based on a pre-loaded database, dynamically adapting output according to sliders configuration.
Laptop Node: This node is used for Camera and Voice modes, leveraging OpenCV and Mediapipe libraries to recognize hand gestures and the Speech Recognition library to process voice commands. This node interfaces with the Arduino Uno to control the robotic hand based on recognized gestures and voice inputs.
