import web
import json


urls = (
    '(.*)/start', 'Start',
    '(.*)/reset', 'Reset'
)

app_drive_stp = web.application(urls, locals())


class Start:
    def POST(self, path):
        try:
            web_dict = json.loads(web.data())
            print web_dict

            steps = web_dict['steps']

            # TODO Call ET-Interface

            web.header('Content-type', 'text/json')
            web.ok()
        except (TypeError, ValueError, AttributeError) as e:
            web.header('Content-type', 'text/html')
            web.notacceptable()
            return e.message


class Reset:
    def POST(self, path):
        # TODO Call ET-Interface

        web.header('Content-type', 'text/json')
        web.ok()