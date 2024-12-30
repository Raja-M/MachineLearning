import serial.tools.list_ports


ports =serial.tools.list_ports.comports()

serialInst = serial.Serial()
portsList = []

for one in ports:
    portsList.append(str(one))
    print(str(one))

com = input( " select com port for Arduino # : ")

for i in range( len( portsList)):
    if portsList[i].startswith( "COM" + str(com)):
        useport = "COM" + str(com)
        print ( " using port : " + useport)

serialInst.baudrate = 9600
serialInst.port = useport
serialInst.open()

while True:
    command = input( " Arduino command (ON/OFF/exit) : ")
    serialInst.write( command.encode('utf-8'))

    if command == 'exit':
        exit()