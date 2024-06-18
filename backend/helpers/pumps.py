from RPi import GPIO
import time

# 100 milliliters = 85 seconds
# 1 milliliter = 0.85 seconds
class Pumps:
    def __init__(self, m1=20, m2=21, m3=16, m4=12) -> None:
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
# if __name__ == "__main__":
#     try:
#         pumps = Pumps()
#         amount = 2
#         amount = amount * 0.85 * 3# 1 milliliter = 0.85 seconds; 1 second = 30 milliliters; 30 milliliters = +- 1 oz
#         # print(amount)
#         pumps.pump_on(0)
#         time.sleep(amount)
#         pumps.pump_off(0)
#         amount = .5
#         amount = amount * 0.85 * 3
#         pumps.pump_on(3)
#         time.sleep(amount)
#         pumps.pump_off(3)
#     except KeyboardInterrupt:
#         print("Quitting...")
#     finally:
#         del pumps
#         print("Cleaning up Pi")


if __name__ == "__main__":
    try:
        pumps = Pumps()
        amount = 2
        amount = amount * 0.85 * 3# 1 milliliter = 0.85 seconds; 1 second = 30 milliliters; 30 milliliters = +- 1 oz
        # print(amount)
        pumps.pump_all_on()
        time.sleep(amount)
        pumps.pump_all_off()
        
    except KeyboardInterrupt:
        print("Quitting...")
    finally:
        del pumps
        print("Cleaning up Pi")