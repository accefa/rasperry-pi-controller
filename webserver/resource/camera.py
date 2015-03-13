import json
import os
import socket

import web
from detection import detectionconfig
from detection.detectionconfig import DetectionConfig


urls = (
    "(.*)", "Camera"
)

app_camera = web.application(urls, locals())

CONFIG_KEY = 'config'
IMAGE_KEY = 'image'

class Camera:
    def GET(self, path):
        try:
            config_dict = DetectionConfig().get_as_dict()
            image_url = self.get_image_url(config_dict[detectionconfig.IMAGE_PATH_KEY])
            response_dict = {
                CONFIG_KEY: config_dict,
                IMAGE_KEY: image_url
            }
            response_dict[CONFIG_KEY].pop(detectionconfig.IMAGE_PATH_KEY)

            web.header('Content-type', 'text/json')
            web.ok()
            return json.dumps(response_dict)
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

    def get_image_url(self, image_path):
        image_name = os.path.basename(image_path)
        host_address = socket.gethostbyname(socket.gethostname())
        return 'http://{0}/image/{1}'.format(host_address, image_name)