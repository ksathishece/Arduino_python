import pyfirmata
import time

#board = pyfirmata.Arduino('COM4')
board = pyfirmata.Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()

button = board.get_pin('d:10:i')
led    = board.get_pin('d:12:o')

while True:

    buttonpress = board.digital[10].read()

    if buttonpress is True:
        led.write(1)
    else:
        led.write(0)
    time.sleep(0.1)






