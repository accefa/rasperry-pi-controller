import json

import web


urls = (
    "(.*)", "Camera"
)

app_camera = web.application(urls, locals())

CONFIG_FILE_PATH = 'config.json'


class Camera:
    def GET(self, path):
        try:
            with open(CONFIG_FILE_PATH) as config_file:
                config = json.load(config_file)

            web.header('Content-type', 'text/json')
            web.ok()
            return json.dumps(config)
        except (TypeError, ValueError) as e:
            print e.message
            web.header('Content-type', 'text/json')
            web.internalerror()

    def PUT(self, path):
        try:
            json_data = web.data()
            config = json.loads(json_data)

            with open(CONFIG_FILE_PATH, 'w') as config_file:
                json.dump(config, config_file)

            web.header('Content-type', 'text/json')
            web.ok()
        except (TypeError, ValueError) as e:
            print e.message
            web.header('Content-type', 'text/json')
            web.notacceptable()