from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

led_pins = [17,18,27,22,23]

for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)

@app.route('/led/<num>')
def control_led(num):

    n = int(num)-1

    for i in range(5):
        GPIO.output(led_pins[i],0)

    if 0 <= n < 5:
        GPIO.output(led_pins[n],1)

    return "LED "+num+" ON"

app.run(host='0.0.0.0',port=5000)
