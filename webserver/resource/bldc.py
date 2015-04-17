import json
import platform

import web


urls = (
    '(.*)/start', 'Start',
    '(.*)/stop', 'Stop',
    '(.*)/reset', 'Reset'
)

app_drive_bldc = web.application(urls, locals())


class Start:
    def POST(self, path):
        try:
            web_dict = json.loads(web.data())

            rpm = web_dict['rpm']

            if rpm < 0:
                raise ValueError

            bldc_serial = get_bldc_serial()
            bldc_serial.start(rpm)

            web.header('Content-type', 'text/json')
            web.ok()
        except (TypeError, ValueError, AttributeError) as e:
            web.header('Content-type', 'text/html')
            web.notacceptable()
            return e.message


class Stop:
    def POST(self, path):
        bldc_serial = get_bldc_serial()
        bldc_serial.stop()

        web.header('Content-type', 'text/json')
        web.ok()


class Reset:
    def POST(self, path):
        bldc_serial = get_bldc_serial()
        bldc_serial.reset()

        web.header('Content-type', 'text/json')
        web.ok()


def get_bldc_serial():
    bldc_serial_class_name = 'BldcSerial'
    bldc_serial_base_module = 'piserial.bldc'

    if platform.system() == 'Linux':
        bldc_serial_module = __import__(bldc_serial_base_module + '.' + 'bldc_serial',
                                        fromlist=[bldc_serial_class_name])
    else:
        bldc_serial_module = __import__(bldc_serial_base_module + '.' + 'bldc_stub', fromlist=[bldc_serial_class_name])

    return getattr(bldc_serial_module, bldc_serial_class_name)