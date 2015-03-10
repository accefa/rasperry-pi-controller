import json

import web
from detection.detectionconfig import DetectionConfig


urls = (
    "(.*)", "Camera"
)

app_camera = web.application(urls, locals())

CONFIG_FILE_PATH = 'config.json'


class Camera:
    def GET(self, path):
        try:
            with open(CONFIG_FILE_PATH) as config_file:
                config_dict = json.load(config_file)

            web.header('Content-type', 'text/json')
            web.ok()
            return json.dumps(config_dict)
        except (TypeError, ValueError) as e:
            print e.message
            web.header('Content-type', 'text/json')
            web.internalerror()

    def PUT(self, path):
        try:
            json_data = web.data()
            config_dict = json.loads(json_data)

            detection_config = DetectionConfig()
            detection_config.set_from_dict(config_dict)

            with open(CONFIG_FILE_PATH, 'w') as config_file:
                json.dump(detection_config.get_as_dict(), config_file, indent=2)

            web.header('Content-type', 'text/json')
            web.ok()
        except (TypeError, ValueError) as e:
            print e.message
            web.header('Content-type', 'text/json')
            web.notacceptable()