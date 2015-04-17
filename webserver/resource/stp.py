import platform
import json

import web


urls = (
    '(.*)/start', 'Start',
    '(.*)/reset', 'Reset'
)

app_drive_stp = web.application(urls, locals())


class Start:
    def POST(self, path):
        try:
            web_dict = json.loads(web.data())

            steps = web_dict['steps']

            stp_serial = get_stp_serial()
            stp_serial.start(steps)

            web.header('Content-type', 'text/json')
            web.ok()
        except (TypeError, ValueError, AttributeError) as e:
            web.header('Content-type', 'text/html')
            web.notacceptable()
            return e.message


class Reset:
    def POST(self, path):
        stp_serial = get_stp_serial()
        stp_serial.reset()

        web.header('Content-type', 'text/json')
        web.ok()


def get_stp_serial():
    stp_serial_class_name = 'StpSerial'
    stp_serial_base_module = 'piserial.stp'

    if platform.system() == 'Linux':
        stp_serial_module = __import__(stp_serial_base_module + '.' + 'stp_serial', fromlist=[stp_serial_class_name])
    else:
        stp_serial_module = __import__(stp_serial_base_module + '.' + 'stp_stub', fromlist=[stp_serial_class_name])

    return getattr(stp_serial_module, stp_serial_class_name)