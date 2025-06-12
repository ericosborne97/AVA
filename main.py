import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#define the gpio of each motor3
motor_1_pwm  = 8
motor_1_dir_1 = 9
motor_1_dir_2 = 7

#Set mode and all pins to output

GPIO.setup(motor_1_pwm, GPIO.OUT)
GPIO.setup(motor_1_dir_1, GPIO.OUT)
GPIO.setup(motor_1_dir_2, GPIO.OUT)

#Configure all motors to run at 100 pwm
speed = 10

motor_1_pwm_gpio = GPIO.PWM(motor_1_pwm, speed)

#Sanity check because sometimes pwm can remain on after program has ended
motor_1_pwm_gpio.stop()

while True:
    motor_1_pwm_gpio.start(speed)
    GPIO.output(motor_1_dir_1, GPIO.LOW)
    GPIO.output(motor_1_dir_2, GPIO.HIGH)

GPIO.cleanup()

