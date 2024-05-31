from RPi import GPIO
from time import sleep, time
import os

button = 22
hold_time = 5  # seconds
press_time = 0

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(button, GPIO.BOTH, callback=button_press, bouncetime=200)

def button_press(channel):
    global press_time
    if GPIO.input(button) == GPIO.LOW:  # Button pressed
        press_time = time()
    else:  # Button released
        if time() - press_time >= hold_time:
            print("Shutting down...")
            os.system("sudo shutdown -h now")

try:
    setup()
    while True:
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Goodbye!")
