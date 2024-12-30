from asyncore import write

from pyfirmata2 import Arduino, ArduinoMega
import time

board = ArduinoMega( "COM5" )
red=7
yel=5
gre=3
lon=1
lof=0
print ( board.get_firmata_version() )
for i in range(0, 3):
    board.digital[red].write(lon)
    time.sleep(2)
    board.digital[red].write(lof)
    board.digital[gre].write(lon)
    time.sleep(2)
    board.digital[gre].write(lof)
    board.digital[yel].write(lon)
    time.sleep(1)
    board.digital[yel].write(lof)


board.digital[red].write(lof)
board.digital[gre].write(lof)
board.digital[yel].write(lof)
