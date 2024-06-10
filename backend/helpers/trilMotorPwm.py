import RPi.GPIO as GPIO
from time import sleep

class DCMotor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 1000)  # Set PWM frequency to 1000Hz
        self.pwm.start(0)  # Start with 0% duty cycle

    def changeSpeed(self, percentage):
        self.pwm.ChangeDutyCycle(percentage)

    def stop(self):
        self.pwm.ChangeDutyCycle(0)

    def cleanup(self):
        self.stop()
        self.pwm.stop()
        GPIO.cleanup()

# example usage
# if __name__ == "__main__":
#     try:
#         motor = DCMotor(12)
#         while True:
#             print("Turning on motor")
#             for i in range(0, 101, 5):
#                 motor.changeSpeed(i)
#                 sleep(0.1)
#             print("Motor at its max speed")
#             sleep(10)
#             print("Turning off motor")
#             for i in range(100, -1, -5):
#                 motor.changeSpeed(i)
#                 sleep(0.1)
#             print("Motor stopped")
#             sleep(5)
#     except KeyboardInterrupt as e:
#         motor.cleanup()
#         print("\nQuitting...")

if __name__ == "__main__":
    try:
        motor = DCMotor(25)
        while True:
            print("Turning on motor")
            motor.changeSpeed(100)
            sleep(10)
            print("Turning off motor")
            motor.stop()
            sleep(5)
    except KeyboardInterrupt as e:
        motor.cleanup()
        print("\nQuitting...")