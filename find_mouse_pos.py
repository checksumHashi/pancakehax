from pynput import mouse, keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
from time import sleep
mouse = mouse.Controller()
while(True):
    print('The current pointer position is {0}'.format(mouse.position))
    sleep(3)