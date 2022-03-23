#!/usr/bin/env python3
import subprocess
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

class photo:
    def save_to_sd(self):
        test = subprocess.Popen(["gphoto2", "--set-config", "capturetarget=1"], stdout=subprocess.PIPE)
        #run the subprocess and capture standard output
        output = test.communicate()[0]
    def take_picture(self):
        test = subprocess.Popen(["gphoto2", "--trigger-capture"], stdout=subprocess.PIPE)
        #run the subprocess and capture standard output
        output = test.communicate()[0]

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set

Shoot = photo()
Shoot.save_to_sd()

while True:
    if GPIO.input(10) == GPIO.HIGH:
        Shoot.take_picture()
