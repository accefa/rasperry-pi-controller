class BldcSerial:
    def __init__(self):
        pass

    @staticmethod
    def start(rpm):
        print 'SERIAL: BLDC gestartet mit ' + str(rpm) + " RPM"

    @staticmethod
    def stop():
        print 'SERIAL: BLDC gestoppt'

    @staticmethod
    def reset():
        print 'SERIAL: BLDC geresetet'
