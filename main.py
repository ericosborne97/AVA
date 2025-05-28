import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#define your specific motor pwm pins here
motor1pin = 9
motor2pin = 2
motor3pin = 3
motor4pin = 4
motor5pin = 5
motor6pin = 6
motor7pin = 7
motor8pin = 8

GPIO.setup(motor1pin, GPIO.OUT)

GPIO.PWM(motor1pin, 50)