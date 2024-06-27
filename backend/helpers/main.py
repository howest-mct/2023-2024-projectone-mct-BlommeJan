import RPi.GPIO as GPIO
from time import sleep, time
# from helpers.kleur import Kleur as kleur
# from helpers.lcdPcf import lcd as lcd
from helpers.trilMotorPwm import DCMotor as vibrator
from helpers.onewire import OneWire as onewire
from helpers.pumps import Pumps as pump
# from helpers.servomotor import ServoMotor as servo
from helpers.UltraSonic import HC_SR04 as ultrasonic
import os

class Main:
    def __init__(self) -> None:
        self.setup()
        self.start()

    #-----------------------------------#
    #               start               #
    #-----------------------------------#

    def setup(self):
        # self.kleur = kleur(s0=5, s1=6, s2=13, s3=19, out=26)
        # # self.lcd = lcd()
        self.vibrator = vibrator(25)
        self.onewire = onewire("28-8590fd1d64ff")
        # self.pump = pump(address=0x3c) 
        self.pump = pump(m1=12, m2=16, m3=20, m4=21)
        # # self.servo = servo(18)
        self.ultrasonic = ultrasonic(17,27)

    def start(self):
        pass
        # # self.lcd.lcd_clear()
        # # self.lcd.lcd_display_string("Dionyshake", 1, 2)
        # # self.lcd.lcd_display_string("Let's drink!", 2, 2)

    #-----------------------------------#
    #              actions              #
    #-----------------------------------#    

    def close_lid(self):
        pass
        # self.servo.set_angle(0)

    def open_lid(self):
        pass
        # self.servo.set_angle(80)

    def pump_amount(self,pump, amount):
        amount = amount * 0.85 * 30# 1 milliliter = 0.85 seconds; 1 second = 30 milliliters; 30 milliliters = +- 1 oz
        self.pump.pump_on(pump)
        sleep(amount)
        self.pump.pump_off(pump)

    def clean_pump(self):
        self.pump.pump_all_on()
        sleep(5)
        self.pump.pump_all_off()

    def get_color(self) -> str:
        pass
    
    def get_temp(self) -> float:
        return self.onewire.read_temperature()
    
    def cup_available(self) -> float:
        value = self.ultrasonic.distance()
        if value < 5:
            return 1
        else:
            return 0
        
    def shake(self, duration):
        for i in range(0, 26, 5):
            vibrator.changeSpeed(i)
            sleep(0.1)
        sleep(duration)
        for i in range(26, -1, -5):
            vibrator.changeSpeed(i)
            sleep(0.1)

    #-----------------------------------#
    #            application            #
    #-----------------------------------#

    # def make_cocktail(self, duration, bottle1, amount1, bottle2 = None, amount2 = None, bottle3 = None, amount3 = None, bottle4 = None, amount4 = None):
    def make_cocktail(self):
        print("Making cocktail")    
        # if self.cup_available(): # check if cup is available but this for some reason does not work anymore and always returns 0
        # self.open_lid()
        # self.pump_amount(bottle1, amount1)
        # if bottle2 != None:
        #     self.pump_amount(bottle2, amount2)
        # if bottle3 != None:
        #     self.pump_amount(bottle3, amount3)
        # if bottle4 != None:
        #     self.pump_amount(bottle4, amount4)
        # if duration != 0:
        #     self.close_lid()
        #     self.shake(duration)
        #     self.open_lid()

        pumps = self.pump
        amount = 2
        amount = amount * 0.85 * 3# 1 milliliter = 0.85 seconds; 1 second = 30 milliliters; 30 milliliters = +- 1 oz
        # print(amount)
        pumps.pump_on(0)
        time.sleep(amount)
        pumps.pump_off(0)
        amount = .5
        amount = amount * 0.85 * 3
        pumps.pump_on(3)
        time.sleep(amount)
        pumps.pump_off(3)

    def scan(self, color) -> int:
        # scan_color = self.get_color()
        # if scan_color == color:
        #     return 1
        # else:
        #     return 0
        pass

    def get_temperature(self) -> float:
        return self.get_temp()

    def cleanPumps(self):
        self.clean_pump()
    

    #-----------------------------------#
    #              cleanup              #
    #-----------------------------------#                 

    # def __del__(self):
    #     del self.kleur
    #     # del self.lcd
    #     del self.vibrator
    #     del self.onewire
    #     del self.pump
        # del self.servo
    #     del self.ultrasonic


if __name__ == "__main__":
    try:
        main = Main()
        while True:
            main.cleanPumps()
    except KeyboardInterrupt as e:
        print("\nQuitting...")
    finally:
        del main
        print("Cleaning up Pi")