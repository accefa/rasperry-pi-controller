import platform

import web


urls = (
    '(.*)/forward', 'Forward',
    '(.*)/backward', 'Backward',
    '(.*)/stop', 'Stop',
    '(.*)/reset', 'Reset'
)

app_drive_dc = web.application(urls, locals())


class Forward:
    def POST(self, path):
        dc_serial = get_dc_serial()
        dc_serial.forward()

        web.header('Content-type', 'text/json')
        web.ok()


class Backward:
    def POST(self, path):
        dc_serial = get_dc_serial()
        dc_serial.backward()

        web.header('Content-type', 'text/json')
        web.ok()


class Stop:
    def POST(self, path):
        dc_serial = get_dc_serial()
        dc_serial.stop()

        web.header('Content-type', 'text/json')
        web.ok()


class Reset:
    def POST(self, path):
        dc_serial = get_dc_serial()
        dc_serial.reset()

        web.header('Content-type', 'text/json')
        web.ok()


def get_dc_serial():
    dc_serial_class_name = 'DcSerial'
    dc_serial_base_module = 'piserial.dc'

    if platform.system() == 'Linux':
        dc_serial_module = __import__(dc_serial_base_module + '.' + 'dc_serial', fromlist=[dc_serial_class_name])
    else:
        dc_serial_module = __import__(dc_serial_base_module + '.' + 'dc_stub', fromlist=[dc_serial_class_name])

    return getattr(dc_serial_module, dc_serial_class_name)