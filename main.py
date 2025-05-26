import tkinter as tk
import Jetson.GPIO as GPIO
import time
import threading

# Set up the GPIO pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

# Set up the tkinter window
root = tk.Tk()
root.geometry("500x500")
root.title("AVA")

label = tk.Label(root, text="Hello", font=('Arial', 18))
label.pack(padx=20, pady=20)

# Function to control the GPIO pin
def gpio_control():
    while True:
        GPIO.output(16, GPIO.LOW)  # Turn off GPIO pin
        time.sleep(5)  # Wait for 5 seconds
        GPIO.output(16, GPIO.HIGH)  # Turn on GPIO pin
        time.sleep(5)  # Wait for 5 seconds

# Create and start a new thread for GPIO control
gpio_thread = threading.Thread(target=gpio_control, daemon=True)
gpio_thread.start()

# Start the Tkinter main event loop
root.mainloop()

# Cleanup GPIO on exit
GPIO.cleanup()
