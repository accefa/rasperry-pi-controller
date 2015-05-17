import piserial.util.command as command


class StpSerial:
    def __init__(self):
        pass

    @staticmethod
    def start(steps):
        command.execute("STP on")
        if (steps < 0):
            steps = (-1) * steps
            command.execute("stepper move r " + str(steps))
        else:
            command.execute("stepper move f " + str(steps))


    @staticmethod
    def reset():
        command.execute("stepper reset")
        command.execute("stepper softhiz")
        command.execute("STP reset")
