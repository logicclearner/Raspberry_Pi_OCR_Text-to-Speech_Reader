# Raspberry_Pi_OCR_Text-to-Speech_Reader
A Python script that turns a Raspberry Pi with a camera into a portable text-reading device for the visually impaired.

This project leverages a Raspberry Pi and its camera module to capture images of text, convert that text into a digital string using Optical Character Recognition (OCR), and then read the text aloud using a text-to-speech engine. The application displays a live camera feed, and with a single keypress, it captures an image, processes it, and speaks the contents, making it a powerful assistive technology tool.

Features:
This project's primary feature is its real-time text-to-speech capability, allowing users to hear the contents of a document or sign by simply pointing a camera at it. It provides a live video preview so the user can accurately position the camera over the desired text before capture. The entire process is initiated by a simple keyboard command ('z' key), making it easy to operate. The system is built with widely available and robust open-source libraries, ensuring good performance and customizability.

Hardware and Software Requirements:
The hardware required for this project includes a Raspberry Pi (any model with a camera connector), a Raspberry Pi Camera Module, and a speaker or headphones connected to the Pi's audio output. On the software side, you will need a Raspberry Pi operating system (like Raspberry Pi OS) with Python 3 installed. The project also requires several key libraries: pytesseract for the OCR engine, opencv-python for image processing and displaying the camera feed, pyttsx3 for the text-to-speech functionality, and picamera2 to interface with the camera module. You will also need to install the Tesseract OCR engine itself on the Raspberry Pi.

Getting Started:
Follow these instructions to get the project set up and running on your Raspberry Pi.

1. Installation:
The installation process begins with setting up the necessary software on your Raspberry Pi. First, open the terminal and install the Tesseract OCR engine by running sudo apt-get install tesseract-ocr. Next, you will need to install the required Python libraries using pip. Run the following commands one by one: pip install opencv-python, pip install pytesseract, pip install pyttsx3, and pip install picamera2. Ensure your Raspberry Pi Camera is enabled in the Raspberry Pi configuration settings (raspi-config).

2. Usage:
To run the application, navigate to the directory containing the Python script in your terminal and execute it with the command: python your_script_name.py. A window titled "Capturing" will appear, showing the live feed from your camera. Position the camera so that the text you want to read is clearly visible in the frame. Press the 'z' key on your keyboard to capture the image. The script will then process the image, print the extracted text to the terminal, and speak the text aloud through your connected speakers or headphones. The program will exit after reading the text.

How It Works:
The script works by first initializing the Raspberry Pi camera and the text-to-speech engine. It then enters a continuous loop that displays the live camera feed in a window using OpenCV. The program waits for a keypress from the user. When the 'z' key is pressed, the current frame from the camera feed is captured and saved as an image. This captured image is then passed to the Tesseract OCR engine via the pytesseract library, which analyzes the image and extracts any recognizable text into a string. This extracted string is then passed to the pyttsx3 engine, which converts the text to speech and plays it through the audio output. The program then breaks the loop and terminates.

License:
This project is open source. Feel free to use, modify, and distribute it.
