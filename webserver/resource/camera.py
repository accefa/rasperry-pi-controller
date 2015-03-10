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
            config_dict = DetectionConfig().get_as_dict()
            web.header('Content-type', 'text/json')
            web.ok()
            return json.dumps(config_dict)
        except (TypeError, ValueError) as e:
            web.header('Content-type', 'text/html')
            web.internalerror()
            return e.message

    def PUT(self, path):
        try:
            config_dict = json.loads(web.data())

            detection_config = DetectionConfig()
            detection_config.set_from_dict(config_dict)

            web.header('Content-type', 'text/json')
            web.ok()
            return json.dumps(detection_config.get_as_dict())
        except (TypeError, ValueError) as e:
            web.header('Content-type', 'text/html')
            web.notacceptable()
            return e.message