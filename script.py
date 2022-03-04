from pynput import mouse, keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
from time import sleep

# position for the discord text box
message_pos = (1349, 1031)
copystart_pos = (1653, 976)
copyend_pos = (1341, 864)
notepad_pos = (428, 793)

# define input devices
mouse = mouse.Controller()
keyboard = keyboard.Controller()

cross = """:xtick:"""

def copylastmessage():
    i=0
    while(i<4):
        mouse.position = copystart_pos
        mouse.press(Button.left)
        mouse.release(Button.left)
        keyboard.press(Key.shift)
        mouse.position = copyend_pos
        mouse.press(Button.left)
        mouse.release(Button.left)
        keyboard.release(Key.shift)
        sleep(0.05)
        keyboard.press(Key.ctrl)
        keyboard.press('c')
        keyboard.release(Key.ctrl)
        keyboard.release('c')
        keyboard.press(Key.ctrl)
        keyboard.press('c')
        keyboard.release(Key.ctrl)
        keyboard.release('c')
        sleep(0.05)
        i+=1
    mouse.position = (428, 793)
    mouse.press(Button.left)
    mouse.release(Button.left)
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release(Key.ctrl)
    keyboard.release('v')
    sleep(0.001)
    keyboard.press(Key.ctrl)
    keyboard.press('s')
    keyboard.release(Key.ctrl)
    keyboard.release('s')
    sleep(0.001)
    keyboard.press(Key.ctrl)
    keyboard.press('s')
    keyboard.release(Key.ctrl)
    keyboard.release('s')
    sleep(0.001)
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release(Key.ctrl)
    keyboard.release('a')
    sleep(0.001)
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)

def sendtext(text):
    mouse.position = message_pos
    mouse.press(Button.left)
    mouse.release(Button.left)
    keyboard.type(text)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    return

def fish():
    sendtext('p!fish')
    sleep(1)
    copylastmessage()
    with open('input.txt', 'r') as inp:
        print('opened input file')
        print('###\n\n', inp.read(), '\n\n###\n')
        print('testing for tick')
        if cross in inp.read():
            print('tick found!')
            sendtext('p!buy fishing rod')
            sleep(1)

    copylastmessage()
    with open('input.txt', 'r') as inp:
        if cross in inp.read():
            print('Found a tick for buying a fishing rod!')
            sendtext('p!withdraw 50')
            sleep(1)
            sendtext('p!buy fishing rod')
            sleep(1)
            sendtext('+:check:')
            sleep(0.1)
            sendtext('+:check:')
            sleep(0.5)
            sendtext('p!fish')
            sleep(0.5)

    sleep(0.5)
    sendtext('p!sell all')
    sleep(1)
    sendtext('+:check:')
    sleep(0.1)
    sendtext('+:check:')
    sleep(0.5)
    sendtext('p!deposit all')
    sleep(0.5)
    return
    
def work():
    sendtext('p!work')
    sleep(1)
    sendtext('p!sell all')
    sleep(1.5)
    sendtext('+:check:')
    sleep(0.1)
    sendtext('+:check:')
    sleep(0.5)
    sendtext('p!deposit all')
    sleep(0.5)
    return

def main():
    ticks = {
        'fish': 0,
        'work': 0
    }
    fish()
    work()
    while(True):
        try:
            if ticks['fish'] >= (60 + 3):
                fish()
                ticks['fish'] = 0
            if ticks['work'] >= (60 * 5 + 3):
                work()
                ticks['work'] = 0
            for key in ticks:
                ticks[key] += 1
            print(ticks)
            sleep(1)
        except:
            pass

main()