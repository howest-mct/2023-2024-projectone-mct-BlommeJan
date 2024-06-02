from RPi import GPIO
from smbus import SMBus
import time

class Pcf8574:
    """PCF Class
    The PCF8574 component is an I/O expander that can be used to get more pins using the i2c bus.

    Address can be found by running i2cdetect -y 1 on the PI when pins are plugged into SDA1 and SCL1.
    By using the write_byte function you can change the state of each send/receive data pin.
    for example write_byte(0b10101010) will set the pins P0, P2, P4 and P6 to HIGH and the other pins to LOW.

    Pins (RIGHT SIDE, INDENT ON TOP):
    pin 1 (VCC): 3.3v
    pin 2 (SDA): PI: SDA1
    pin 3 (SCL): PI: SCL1
    pin 4:
    pin 5 (P7): Used to send/receive data
    pin 6 (P6): Used to send/receive data
    pin 7 (P5): Used to send/receive data
    pin 8 (P4): Used to send/receive data

    Pins (LEFT SIDE, INDENT ON TOP):
    pin 1 (A0): GROUND
    pin 2 (A1): GROUND
    pin 3 (A2): GROUND
    pin 4 (P0): Used to send/receive data
    pin 5 (P1): Used to send/receive data
    pin 6 (P2): Used to send/receive data
    pin 7 (P3): Used to send/receive data
    pin 8 (GND): GROUND
    """

    def __init__(self, address=0x20):
        self.i2c = SMBus()
        self.i2c.open(1)
        self.address = address

    # value = 8 bit binary value: 0b00000000
    def write_byte(self, value):
        self.i2c.write_byte(self.address, value)

    def read_byte(self):
        return self.i2c.read_byte(self.address)

    def __del__(self):
        self.i2c.close()

def motor_control(pcf, value):
    """Control motors using a binary value."""
    pcf.write_byte(value)

if __name__ == "__main__":
    try:
        pcf = Pcf8574()

        # Example usage
        while True:
            # Turn on motor 2 (binary 0010)
            motor_control(pcf, 0b00000010)
            time.sleep(2)

            # Turn on motor 1 and motor 4 (binary 1001)
            motor_control(pcf, 0b00001001)
            time.sleep(2)

            # Turn off all motors (binary 0000)
            motor_control(pcf, 0b00000000)
            time.sleep(2)

            # Turn on all motors (binary 1111)
            motor_control(pcf, 0b00001111)
            time.sleep(2)

    except KeyboardInterrupt as k:
        print("Program stopped by user")
        print(k)
        GPIO.cleanup()
        # Delete class instance to close the i2c bus
        del pcf
        GPIO.cleanup()
