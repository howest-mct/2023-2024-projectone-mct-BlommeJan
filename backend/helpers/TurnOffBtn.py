from RPi import GPIO
from time import sleep, time
# from lcdPcf import lcd as lcd
from ip import IPAddress
import os

class ButtonHandler:
    def __init__(self, button_pin, ip_time=0.5, kill_time=5):
        self.button_pin = button_pin
        self.ip_time = ip_time
        self.kill_time = kill_time
        self.press_time = 0
        self.ip = IPAddress()  # Instantiate IPAddress here
        # self.lcd = lcd()
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.button_pin, GPIO.BOTH, callback=self.button_press, bouncetime=200)

    def button_press(self, channel):
        if GPIO.input(self.button_pin) == GPIO.LOW:  # Button pressed
            self.press_time = time()
        else:  # Button released
            if time() - self.press_time >= self.kill_time:  # Button held for 5 seconds
                print("Shutting down...")
                # self.lcd.lcd_clear()
                # self.lcd.lcd_display_string("BYE  BYE", 1, 4)
                # self.lcd.lcd_display_string("Shutting down...", 2)
                os.system("sudo shutdown -h now")

            elif time() - self.press_time >= self.ip_time:
                print("IP address")
                print(self.ip())  # Call the IPAddress instance
                # self.lcd.lcd_clear()
                # self.lcd.lcd_display_string("IP Address:", 1)
                # self.lcd.lcd_display_string(self.ip(), 2)
                

    def cleanup(self):
        GPIO.cleanup()

if __name__ == "__main__":
    button = ButtonHandler(22)
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        button.cleanup()