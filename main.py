import tkinter as tk
import Jetson.GPIO as GPIO
import time

root = tk.Tk()

#set window attributes
root.geometry("500x500")
root.title("AVA")

label = tk.Label(root, text="Hello", font=('Arial',18))
label.pack(padx=20,pady=20)

#opens a window
root.mainloop()

GPIO.setmode(GPIO.BOARD)         # use physical pin numbers
LED = 12                         # J41 pin 12 (BCM 18)

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(0.5)
finally:
    GPIO.cleanup()               # always reset pins on exit
