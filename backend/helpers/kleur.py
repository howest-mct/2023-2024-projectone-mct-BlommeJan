import RPi.GPIO as GPIO
import time

# Pin definitions
s0 = 5
s1 = 6
s2 = 13
s3 = 19
out = 26

# Initialize RGB values
Red = 0
Blue = 0
Green = 0

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(s0, GPIO.OUT)
    GPIO.setup(s1, GPIO.OUT)
    GPIO.setup(s2, GPIO.OUT)
    GPIO.setup(s3, GPIO.OUT)
    GPIO.setup(out, GPIO.IN)
    
    # Set frequency scaling to 100%
    GPIO.output(s0, GPIO.HIGH)
    GPIO.output(s1, GPIO.HIGH)
    
    print("Setup complete")

def get_color():
    global Red, Blue, Green
    
    # Measure RED
    GPIO.output(s2, GPIO.LOW)
    GPIO.output(s3, GPIO.LOW)
    Red = pulse_in(out, GPIO.HIGH)
    time.sleep(0.02)
    
    # Measure BLUE
    GPIO.output(s3, GPIO.HIGH)
    Blue = pulse_in(out, GPIO.HIGH)
    time.sleep(0.02)
    
    # Measure GREEN
    GPIO.output(s2, GPIO.HIGH)
    Green = pulse_in(out, GPIO.HIGH)
    time.sleep(0.02)

def pulse_in(pin, level, timeout=1000000):
    start_time = time.time()
    while GPIO.input(pin) != level:
        if (time.time() - start_time) > timeout / 1000000.0:
            return 0

    start = time.time()
    while GPIO.input(pin) == level:
        if (time.time() - start_time) > timeout / 1000000.0:
            return 0
    end = time.time()
    return (end - start) * 1000000  # Convert to microseconds

def identify_color(R, G, B):
    # Based on the values of R, G, and B, define the color
    if R <= 15 and G <= 15 and B <= 15:
        return "White"
    elif R < B and R <= G and R < 23:
        return "Red"
    elif B < G and B < R and B < 20:
        return "Blue"
    elif G < R and G - B <= 8:
        return "Green"
    # Add additional color logic here:
    elif R > 100 and G > 50 and B < 50:
        return "Orange"
    elif R > 100 and G > 100 and B < 50:
        return "Yellow"
    elif R > 50 and G < 50 and B > 50:
        return "Purple"
    elif R > 200 and G > 150 and B > 150:
        return "Pink"
    elif R > 100 and G < 50 and B < 50:
        return "Brown"
    elif R > 200 and G > 200 and B > 200:
        return "See-Through"
    else:
        return "Unknown"

def scan_colors(scan_duration=10, interval=0.5):
    red_values = []
    green_values = []
    blue_values = []

    start_time = time.time()
    while time.time() - start_time < scan_duration:
        get_color()
        red_values.append(Red)
        green_values.append(Green)
        blue_values.append(Blue)
        time.sleep(interval)

    avg_red = sum(red_values) / len(red_values)
    avg_green = sum(green_values) / len(green_values)
    avg_blue = sum(blue_values) / len(blue_values)

    return identify_color(avg_red, avg_green, avg_blue)

if __name__ == "__main__":
    setup()
    try:
        while True:
            final_color = scan_colors(scan_duration=10, interval=0.5)
            print(f"Final color: {final_color}")
            time.sleep(2)  # Delay before the next scan
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Program terminated")