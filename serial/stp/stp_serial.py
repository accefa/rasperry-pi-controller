class StpSerial:
    def __init__(self):
        pass

    @staticmethod
    def start(steps):
        print 'SERIAL: STP faehrt um ' + str(steps) + ' Schritte'

    @staticmethod
    def reset():
        print 'SERIAL: STP geresetet'
