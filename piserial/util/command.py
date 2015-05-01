import time

import serial


DEVICE = "/dev/ttyACM0"
BAUDRATE = 38400
TIMEOUT = 2

def execute(command):
    print("Debug: Execute " + command)
    ser = serial.Serial(port=DEVICE, baudrate=BAUDRATE, timeout=TIMEOUT)
    if ser.isOpen() is True:
        print("Serial is open")
        __send_to_serial(command, ser)
        ser.close()
    else:
        print("Serial was not open. So nothing happens.")


def __send_to_serial(cmd, ser):
    cmd += "\n"
    term = "accefa>"
    ser.write(cmd.encode('utf-8'))
    ser.flush()
    time.sleep(1)
    answer = ser.read(1000)
    print("answer: " + answer)
    print("start waiting")
    maxIteration = 8
    counter = 0
    while answer.find(term.encode('utf-8')) < 0:
        if counter > maxIteration:
            break
        counter = counter + 1
        answer = answer.decode('utf-8')
        answer = answer.replace("\n", "")
        print("still waiting");
        if answer != "":
            print("\t" + answer)
        answer = ser.read(1000)
    