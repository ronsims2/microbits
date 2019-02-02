from microbit import *

img = Image.HAPPY

while True:
    img = Image.HAPPY if img != Image.HAPPY else Image.SAD
    if pin0.read_digital():
        display.show(img)
    sleep(0.8)