import RPi.GPIO as GPIO
from time import sleep, time
from kleur import Kleur as kleur
from lcdPcf import lcd as lcd
from trilMotorPwm import DCMotor as vibrator
from onewire import ow as onewire
from pumps import Pcf8574 as pump
from servomotor import ServoMotor as servo
from UltraSonic import HC_SR04 as ultrasonic
import os

class Main:
    def __init__(self) -> None:
        self.setup()

    def setup(self):
        self.kleur = kleur(s0=5, s1=6, s2=13, s3=19, out=26)
        self.lcd = lcd()
        self.vibrator = vibrator(25)
        self.onewire = onewire("28-8590fd1d64ff")
        self.pump = pump(adress=0x3c) 
        self.servo = servo(18)
        self.ultrasonic = ultrasonic(17,27)

    