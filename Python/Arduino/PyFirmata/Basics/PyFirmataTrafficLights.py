from asyncore import write

from pyfirmata2 import Arduino, ArduinoMega
import time

board = ArduinoMega( "COM5" )
fred=33
fyell=45
fgree=51
rred=8
ryell=6
rgree=4
lon=1
loff=0
print ( board.get_firmata_version() )

loopTimes = input( 'how many times would you like the LED to blink : ')
print ( " Blinking " + loopTimes + " times.")

for x in range( int(loopTimes)):
      print( x )
      board.digital[fred].write(lon)
      time.sleep(0.5)
      board.digital[rgree].write(lon)
      board.digital[rred].write(loff)
      time.sleep(5)
      board.digital[rgree].write(loff)

      board.digital[ryell].write(lon)
      time.sleep(0.5)
      board.digital[ryell].write(loff)

      board.digital[rred].write(lon)
      time.sleep(0.5)
      board.digital[fgree].write(lon)
      board.digital[fred].write(loff)
      time.sleep(5)


      board.digital[fgree].write(loff)
      board.digital[fyell].write(lon)
      time.sleep(0.5)
      board.digital[fyell].write(loff)

board.digital[fgree].write(loff)
board.digital[rgree].write(loff)
board.digital[fyell].write(loff)
board.digital[ryell].write(loff)
board.digital[fred].write(loff)
board.digital[rred].write(loff)
