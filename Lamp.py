import RPi.GPIO as GPIO
import time
from datetime import datetime

# Define the GPIO pin for the relay
relay_pin = 23

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

# Function to turn on the lamp
def turn_on_lamp():
    GPIO.output(relay_pin, GPIO.HIGH)
    print("Lamp is ON")

# Function to turn off the lamp
def turn_off_lamp():
    GPIO.output(relay_pin, GPIO.LOW)
    print("Lamp is OFF")

try:
    lamp_on = False
    while True:
        current_time = datetime.now()

        # Check if it's 5 AM and the lamp is not already on
        if current_time.hour == 5 and current_time.minute == 0 and not lamp_on:
            turn_on_lamp()
            lamp_on = True

        # Wait for input to turn off the lamp
        if lamp_on:
            user_input = input("Type 'woke' to turn off the lamp: ")
            if user_input.strip().lower() == "woke":
                turn_off_lamp()
                lamp_on = False

        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    GPIO.cleanup()
    print("GPIO cleaned up. Bye!")
