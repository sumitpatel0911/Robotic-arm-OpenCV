$Robotic-arm-OpenCV
In this project, we control a Robotic Arm using OpenCV and the cvlearn library.

In this project, we establish serial communication between a Python code and Arduino code.

In Python, we use three modules: OpenCV, cvlearn, and serial. The OpenCV module's task is to detect a live feed. The cvlearn module is based on the Mediapipe module, which counts our fingers. The serial module's task is to send the detected finger values to the Arduino code.

In the Arduino code, we fix every servo position, and they are called according to the incoming serial data.

here, we provide a semple running vedio of a this project:->

https://github.com/sumitpatel0911/Robotic-arm-OpenCV/assets/149647517/4e1c6672-32bf-4e5d-bb36-ae08da9dbe29

