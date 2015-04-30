import time

import serial


DEVICE = '/dev/ttyACM0'
BAUDRATE = 38400


def execute(command):
    ser = serial.Serial(DEVICE, BAUDRATE)
    if ser.isOpen() is True:
        __send_to_serial(command, ser)
    ser.close()


def __send_to_serial(cmd, ser):
    cmd += '\n\n'
    term = 'accefa>'
    ser.write(cmd.encode('utf-8'))
    time.sleep(1)
    answer = ser.readline()
    print("start waiting")
    while answer.find(term.encode('utf-8')) < 0:
        answer = answer.decode('utf-8')
        answer = answer.replace('\n', '')
        print("still waiting");
        if answer != '':
            print("\t" + answer)
        answer = ser.readline()