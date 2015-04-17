import piserial.util.command as command


class BldcSerial:
    def __init__(self):
        pass

    @staticmethod
    def start(rpm):
        command.execute('BLDC on')
        command.execute('BLDC setrpm ' + str(rpm))

    @staticmethod
    def stop():
        command.execute('BLDC off')

    @staticmethod
    def reset():
        command.execute('BLDC reset')

