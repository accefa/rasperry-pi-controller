import web
import json


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

            # TODO Call ET-Interface

            web.header('Content-type', 'text/json')
            web.ok()
        except (TypeError, ValueError, AttributeError) as e:
            web.header('Content-type', 'text/html')
            web.notacceptable()
            return e.message


class Stop:
    def POST(self, path):
        # TODO Call ET-Interface

        web.header('Content-type', 'text/json')
        web.ok()


class Reset:
    def POST(self, path):
        # TODO Call ET-Interface

        web.header('Content-type', 'text/json')
        web.ok()