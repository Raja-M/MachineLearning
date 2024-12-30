from pyfirmata2 import Arduino, ArduinoMega
import time

board = ArduinoMega( "COM5" )

print ( board.get_firmata_version() )

loopTimes = input( 'how many times would you like the LED to blink : ')
print ( " Blinking " + loopTimes + " times.")

for x in range( int(loopTimes)):
      print( x )
      board.digital[4].write(1)
      board.digital[6].write(1)
      board.digital[8].write(1)

      board.digital[51].write(1)
      board.digital[45].write(1)
      board.digital[33].write(1)
      #
      time.sleep(1)
      #
      board.digital[4].write(0)
      board.digital[6].write(0)
      board.digital[8].write(0)

      board.digital[51].write(0)
      board.digital[45].write(0)
      board.digital[33].write(0)

      time.sleep(1)