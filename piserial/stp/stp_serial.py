import piserial.util.command as command


class StpSerial:
    def __init__(self):
        pass

    @staticmethod
    def start(steps):
        command.execute("STP on")
        command.execute("STP move " + str(steps))


    @staticmethod
    def reset():
        command.execute("STP reset")
