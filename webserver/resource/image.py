import web
import os
from detection.detectionconfig import DetectionConfig

urls = (
    "/(.*)", "Image"
)

app_image = web.application(urls, locals())


class Image:
    def GET(self, file_name):
        extension = file_name.split(".")[-1]

        config = DetectionConfig()

        image_folder = config.image_path
        image_path = os.path.join(image_folder, file_name)

        content_type = {
            "png": "images/png",
            "jpeg": "images/jpeg",
            "jpg": "images/jpeg",
            "gif": "images/gif",
            "ico": "images/x-icon"
        }

        if file_name in os.listdir(image_folder):
            web.header("Content-Type", content_type[extension])
            return open(image_path, "rb").read()
        else:
            raise web.notfound()