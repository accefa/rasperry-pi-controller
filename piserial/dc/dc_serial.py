import piserial.util.command as command


class DcSerial:
    def __init__(self):
        pass

    @staticmethod
    def forward():
        command.execute("DC up")
        command.execute("DC on")

    @staticmethod
    def backward():
        command.execute("DC down")
        command.execute("DC on")

    @staticmethod
    def stop():
        command.execute("DC off")

    @staticmethod
    def reset():
        command.execute("DC reset")