import pyfirmata
import time

board = pyfirmata.Arduino('COM4')

while True:
    board.digital[12].write(1)
    time.sleep(1)
    board.digital[12].write(0)
    time.sleep(1)
