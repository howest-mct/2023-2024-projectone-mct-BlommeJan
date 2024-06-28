from RPi import GPIO #type: ignore
from time import sleep

class DCMotor:
    def __init__(self, pin=25):
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

cocktails = {
    "Rum and Coke": {
        "ingredients": {
            "pump_3": 1.5,  # white rum in oz
            "pump_1": 0,    # vodka in oz
            "pump_2": 0,    # cointreau in oz
            "pump_4": 0     # dry vermouth in oz
            # Add coke
        },
        "shake_duration": 0
    },
    "Screwdriver": {
        "ingredients": {
            "pump_3": 0,    # white rum in oz
            "pump_1": 1.5,  # vodka in oz
            "pump_2": 0,    # cointreau in oz
            "pump_4": 0     # dry vermouth in oz
            # Add orange juice
        },
        "shake_duration": 0
    },
    "Vodka Soda": {
        "ingredients": {
            "pump_3": 0,    # white rum in oz
            "pump_1": 1.5,  # vodka in oz
            "pump_2": 0,    # cointreau in oz
            "pump_4": 0     # dry vermouth in oz
            # Add soda water
        },
        "shake_duration": 0
    },
    "Orange Blossom": {
        "ingredients": {
            "pump_3": 0,    # white rum in oz
            "pump_1": 0,    # vodka in oz
            "pump_2": 0.75, # cointreau in oz
            "pump_4": 0.75  # dry vermouth in oz
            # Add orange juice
        },
        "shake_duration": 30
    },
    "Cointreau and Soda": {
        "ingredients": {
            "pump_3": 0,    # white rum in oz
            "pump_1": 0,    # vodka in oz
            "pump_2": 1.5,  # cointreau in oz
            "pump_4": 0     # dry vermouth in oz
            # Add soda water
        },
        "shake_duration": 0
    },
    "Vodka Martini": {
        "ingredients": {
            "pump_3": 0,    # white rum in oz
            "pump_1": 1.5,  # vodka in oz
            "pump_2": 0,    # cointreau in oz
            "pump_4": 0.5   # dry vermouth in oz
            # No additional ingredients
        },
        "shake_duration": 30
    },
    "Rum Martini": {
        "ingredients": {
            "pump_3": 1.5,  # white rum in oz
            "pump_1": 0,    # vodka in oz
            "pump_2": 0,    # cointreau in oz
            "pump_4": 0.5   # dry vermouth in oz
            # No additional ingredients
        },
        "shake_duration": 30
    },
    "Firery Fanta": {
        "ingredients": {
            "pump_3": 0,    # white rum in oz
            "pump_1": 0,    # vodka in oz
            "pump_2": 1,    # cointreau in oz
            "pump_4": 0   # dry vermouth in oz
            # add coke
        },
        "shake_duration": 0
    }

}

def make_cocktail(cocktail_name, pumps):
    if cocktail_name in cocktails:
        details = cocktails[cocktail_name]
        for pump, amount in details['ingredients'].items():
            if amount > 0:
                pump_index = int(pump.split('_')[1]) - 1  # Extract pump index from key
                time_to_pump = amount * 29.57 * 0.85 / 3  # Convert oz to ml, then to seconds
                pumps.pump_on(pump_index)
                sleep(time_to_pump)
                pumps.pump_off(pump_index)
        if details['shake_duration'] > 0:
            sleep(10)  # Wait for the liquid to settle and the lid to be closed
            motor = DCMotor(25)  # Assuming the motor is connected to GPIO pin 25
            motor.changeSpeed(25) # Start the mo/tor at 25% speed
            sleep(details['shake_duration'])
            motor.stop()
            motor.cleanup()
    else:
        print(f"Cocktail {cocktail_name} not found")

if __name__ == "__main__":
    try:
        pumps = Pumps()
        while True:
            print("Available cocktails:")
            for cocktail in cocktails.keys():
                print(f" - {cocktail}")
            selected_cocktail = input("\nEnter the name of the cocktail you want to make: ").strip().lower()
            selected_cocktail = ' '.join(word.capitalize() for word in selected_cocktail.split())
            make_cocktail(selected_cocktail, pumps)
    except KeyboardInterrupt:
        print("Quitting...")
    finally:
        del pumps
        print("Cleaning up Pi")
