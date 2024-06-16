from RPi import GPIO
import time


class ServoMotor:
    """Servo Motor Class
    This class can be used to control a servo motor.

    set_angle(angle) - set the angle of the servo motor

    The servo motor needs to be connected to 5v, GND and 1 GPIO pin, the default is 21.
    RED: 3.3v
    BROWN: GND
    ORANGE: GPIO pin
    """

    def __init__(self, servo_pin=21):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)  # Disable GPIO warnings
        GPIO.setup(servo_pin, GPIO.OUT)
        self.PWM_servo = GPIO.PWM(servo_pin, 50)
        self.PWM_servo.start(7.5)  # Start at 90 degree position

    # angle: 0 - 180
    def set_angle(self, angle):
        '''
        param angle: int - a (a value between 0 and 180)
        return: None
        
        '''
        duty_cycle = ((angle / 180.0) * 10) + 2.5
        self.PWM_servo.ChangeDutyCycle(duty_cycle)
        time.sleep(0.5)  # Allow time for servo to move

    def cleanup(self):
        self.PWM_servo.stop()
        GPIO.cleanup()


# Example usage:
if __name__ == "__main__":
    servo1 = ServoMotor(18)
    try:
        servo1.set_angle(80)
        time.sleep(5)
        servo1.set_angle(0)
    except KeyboardInterrupt as err:
        print(err)
    finally:
        servo1.cleanup()
        print("Cleaning up Pi")
