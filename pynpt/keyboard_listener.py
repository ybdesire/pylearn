from pynput import keyboard

flag = 0

def on_press(key):
    global flag
    try: k = key.char # single-char keys
    except: k = key.name # other keys
    if key == keyboard.Key.esc: return False # stop listener
    if(k=='1'):# press 1
        flag = 1
    elif(k=='2'):
        flag = 2
    elif(k=='3'):
        flag = 3
    elif(k=='4'):
        flag = 5
    elif(k=='5'):
        flag = 5
    elif(k=='6'):
        flag = 6

lis = keyboard.Listener(on_press=on_press)
lis.start() # start to listen on a separate thread

while(True):
    print(flag)
