import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class LED:
    def __init__(self, pin):
        self.pin = pin
        self.pin_voltage = False
        GPIO.setup(pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, True)
        self.pin_voltage = True
        return self.pin_voltage

    def off(self):
        GPIO.output(self.pin, False)
        self.pin_voltage = False
        return self.pin_voltage

class Button:
    def __init__(self, pin):
        self.pin = pin
        self.pressed = False
        GPIO.setup(self.pin, GPIO.IN)

    def check_button(self):
        button_state = GPIO.input(self.pin)
        if button_state == 1:
            self.pressed = True
            return self.pressed
        elif button_state == 0:
            self.pressed = False
            return self.pressed
