import json
import os
import web
from config import detectionconfig
from config.detectionconfig import DetectionConfig
from detection.detection import Detection 

urls = (
    "(.*)", "Camera"
)

app_camera = web.application(urls, locals())


class Camera:
    def GET(self, path):
        try:
            detectionConfig = DetectionConfig()
            detection = Detection()
            detection.detect(detectionConfig)
            
            config_dict = detectionConfig.get_as_dict()
            image_url = self.get_image_url(config_dict[detectionconfig.IMAGE_PATH_KEY])
            config_dict[detectionconfig.IMAGE_PATH_KEY] = image_url

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
            if detectionconfig.IMAGE_PATH_KEY in config_dict:
                config_dict.pop(detectionconfig.IMAGE_PATH_KEY)
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
        return '/static/{0}'.format(image_name)
