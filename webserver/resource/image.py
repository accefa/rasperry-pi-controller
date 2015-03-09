import web
import os

urls = (
    "/(.*)", "Image"
)

app_image = web.application(urls, locals())

IMAGE_FILE_PATH = os.path.dirname(__file__) + '/../../images'


class Image:
    def GET(self, file_name):
        extension = file_name.split(".")[-1]

        file_path = os.path.join(IMAGE_FILE_PATH, file_name)

        content_type = {
            "png": "images/png",
            "jpg": "images/jpeg",
            "gif": "images/gif",
            "ico": "images/x-icon"}

        if file_name in os.listdir(IMAGE_FILE_PATH):
            web.header("Content-Type", content_type[extension])
            return open(file_path, "rb").read()
        else:
            raise web.notfound()