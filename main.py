import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#define your specific motor pwm pins here
motor_driver_1_ena = 3
motor_driver_1_int_1 = 5
motor_driver_1_int_2 = 7
motor_driver_1_int_3 = 11
motor_driver_1_int_4 = 13
motor_driver_1_enb = 15

motor_driver_2_ena = 19
motor_driver_2_int_1 = 21
motor_driver_2_int_2 = 23
motor_driver_2_int_3 = 29
motor_driver_2_int_4 = 31
motor_driver_2_enb = 33

motor_driver_3_ena = 8
motor_driver_3_int_1 = 10
motor_driver_3_int_2 = 12
motor_driver_3_int_3 = 22
motor_driver_3_int_4 = 24
motor_driver_3_enb = 26

motor_driver_4_ena = 36
motor_driver_4_int_1 = 38
motor_driver_4_int_2 = 40
motor_driver_4_int_3 = 29
motor_driver_4_int_4 = 31
motor_driver_4_enb = 32

pin_to_gpio = {
    3: 2,
    5: 3,
    7: 4,
    8: 14,
    10: 15,
    11: 17,
    12: 18,
    13: 27,
    15: 22,
    16: 23,
    18: 24,
    19: 10,
    21: 9,
    22: 25,
    23: 11,
    24: 8,
    26: 7,
    29: 5,
    31: 6,
    32: 12,
    33: 13,
    35: 19,
    36: 16,
    37: 26,
    38: 20,
    40: 21
}

def board_pin_to_gpio(pin):
    return pin_to_gpio.get(pin, None)

#Convert from pin number to GPIO number
motor_driver_1_ena = board_pin_to_gpio(motor_driver_1_ena)
motor_driver_1_int_1 = board_pin_to_gpio(motor_driver_1_int_1)
motor_driver_1_int_2 = board_pin_to_gpio(motor_driver_1_int_2)
motor_driver_1_int_3 = board_pin_to_gpio(motor_driver_1_int_3)
motor_driver_1_int_4 = board_pin_to_gpio(motor_driver_1_int_4)
motor_driver_1_enb = board_pin_to_gpio(motor_driver_1_enb)

motor_driver_2_ena = board_pin_to_gpio(motor_driver_2_ena)
motor_driver_2_int_1 = board_pin_to_gpio(motor_driver_2_int_1)
motor_driver_2_int_2 = board_pin_to_gpio(motor_driver_2_int_2)
motor_driver_2_int_3 = board_pin_to_gpio(motor_driver_2_int_3)
motor_driver_2_int_4 = board_pin_to_gpio(motor_driver_2_int_4)
motor_driver_2_enb = board_pin_to_gpio(motor_driver_2_enb)

motor_driver_3_ena = board_pin_to_gpio(motor_driver_3_ena)
motor_driver_3_int_1 = board_pin_to_gpio(motor_driver_3_int_1)
motor_driver_3_int_2 = board_pin_to_gpio(motor_driver_3_int_2)
motor_driver_3_int_3 = board_pin_to_gpio(motor_driver_3_int_3)
motor_driver_3_int_4 = board_pin_to_gpio(motor_driver_3_int_4)
motor_driver_3_enb = board_pin_to_gpio(motor_driver_3_enb)

motor_driver_4_ena = board_pin_to_gpio(motor_driver_4_ena)
motor_driver_4_int_1 = board_pin_to_gpio(motor_driver_4_int_1)
motor_driver_4_int_2 = board_pin_to_gpio(motor_driver_4_int_2)
motor_driver_4_int_3 = board_pin_to_gpio(motor_driver_4_int_3)
motor_driver_4_int_4 = board_pin_to_gpio(motor_driver_4_int_4)
motor_driver_4_enb = board_pin_to_gpio(motor_driver_4_enb)

#define what motor driver links with hardware
tire_1_steering_enable = motor_driver_1_enb
tire_1_steering_direction_1 = motor_driver_1_int_3
tire_1_steering_direction_2 = motor_driver_1_int_4

tire_1_rotation_enable = motor_driver_1_ena
tire_1_rotation_direction_1 = motor_driver_1_int_1
tire_1_rotation_direction_2 = motor_driver_1_int_2

tire_2_rotation_enable = motor_driver_2_enb
tire_2_rotation_direction_1 = motor_driver_2_int_3
tire_2_rotation_direction_2 = motor_driver_2_int_4

tire_2_steering_enable = motor_driver_2_ena
tire_2_steering_direction_1 = motor_driver_2_int_1
tire_2_steering_direction_2 = motor_driver_2_int_2

#Set mode and all pins to output
GPIO.setmode(GPIO.BCM)

GPIO.setup(motor_driver_1_ena, GPIO.OUT)
GPIO.setup(motor_driver_1_int_1, GPIO.OUT)
GPIO.setup(motor_driver_1_int_2, GPIO.OUT)
GPIO.setup(motor_driver_1_int_3, GPIO.OUT)
GPIO.setup(motor_driver_1_int_4, GPIO.OUT)
GPIO.setup(motor_driver_1_enb, GPIO.OUT)

GPIO.setup(motor_driver_2_ena, GPIO.OUT)
GPIO.setup(motor_driver_2_int_1, GPIO.OUT)
GPIO.setup(motor_driver_2_int_2, GPIO.OUT)
GPIO.setup(motor_driver_2_int_3, GPIO.OUT)
GPIO.setup(motor_driver_2_int_4, GPIO.OUT)
GPIO.setup(motor_driver_2_enb, GPIO.OUT)

GPIO.setup(motor_driver_3_ena, GPIO.OUT)
GPIO.setup(motor_driver_3_int_1, GPIO.OUT)
GPIO.setup(motor_driver_3_int_2, GPIO.OUT)
GPIO.setup(motor_driver_3_int_3, GPIO.OUT)
GPIO.setup(motor_driver_3_int_4, GPIO.OUT)
GPIO.setup(motor_driver_3_enb, GPIO.OUT)

GPIO.setup(motor_driver_4_ena, GPIO.OUT)
GPIO.setup(motor_driver_4_int_1, GPIO.OUT)
GPIO.setup(motor_driver_4_int_2, GPIO.OUT)
GPIO.setup(motor_driver_4_int_3, GPIO.OUT)
GPIO.setup(motor_driver_4_int_4, GPIO.OUT)
GPIO.setup(motor_driver_4_enb, GPIO.OUT)

#Configure all motors to run at 100 pwm
speed = 10
print("tire_1_steering_enable", tire_1_steering_enable)
print("tire_1_rotation_enable", tire_1_rotation_enable)
print("tire_2_steering_enable", tire_2_steering_enable)
print("tire_2_rotation_enable", tire_2_rotation_enable)

tire_1_steering_enable_pwm = GPIO.PWM(tire_1_steering_enable, speed)
tire_1_rotation_enable_pwm = GPIO.PWM(tire_1_rotation_enable, speed)

tire_2_steering_enable_pwm = GPIO.PWM(tire_2_steering_enable, speed)
tire_2_rotation_enable_pwm = GPIO.PWM(tire_2_rotation_enable, speed)

while True:
    #tire_2_steering_enable_pwm.start(speed)
    GPIO.output(tire_2_steering_direction_1, GPIO.LOW)
    GPIO.output(tire_2_steering_direction_2, GPIO.HIGH)

GPIO.cleanup()
