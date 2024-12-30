from pyfirmata2 import Arduino, ArduinoMega
import time

board = ArduinoMega( "COM5" )

print ( board.get_firmata_version() )
yourchoice = ''



while ( yourchoice != 'exit'):
      yourchoice  = input( " Arduino command (on/off/exit) :")
      print ( " you choose : " + yourchoice)
      if ( yourchoice == 'on'):
            board.digital[2].write(1)
      elif( yourchoice == 'off'):
            board.digital[2].write(0)
      else:
            for i in range(1, 5, 1):
                  board.digital[6].write(1)
                  time.sleep(0.2)
                  board.digital[6].write(0)
                  time.sleep(0.2)
            exit(0)


# loopTimes = input( 'how many times would you like the LED to blink ')
# print ( " Blinking " + loopTimes + " times .")
#
# for x in range( int(loopTimes)):
#       print( x )
#       board.digital[2].write(1)
#       time.sleep(1)
#       board.digital[2].write(0)
#       time.sleep(1)


