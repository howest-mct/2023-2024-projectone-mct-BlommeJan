from RPi import GPIO
import time

# 100 milliliters = 85 seconds
# 1 milliliter = 0.85 seconds
class Pumps:
    def __init__(self, m1=12, m2=16, m3=20, m4=21) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.pins = [m1, m2, m3, m4]
        GPIO.setmode(GPIO.BCM)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)

    def pump_on(self, pump_number):
        GPIO.output(self.pins[pump_number], GPIO.HIGH)

    def pump_off(self, pump_number):
        GPIO.output(self.pins[pump_number], GPIO.LOW)

    def pump_all_on(self):
        for pin in self.pins:
            GPIO.output(pin, GPIO.HIGH)
    
    def pump_all_off(self):
        for pin in self.pins:
            GPIO.output(pin, GPIO.LOW)

    def __del__(self):
        GPIO.cleanup()

# example code
if __name__ == "__main__":
    try:
        pumps = Pumps()
        while True:
            for i in range(4):
                pumps.pump_on(i)
                time.sleep(1)
                pumps.pump_off(i)
                time.sleep(1)
    except KeyboardInterrupt:
        print("Quitting...")
    finally:
        del pumps
        print("Cleaning up Pi")