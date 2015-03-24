import logging
import web
from webserver.resource.camera import app_camera
from webserver.resource.image import app_image
from webserver.resource.start import app_start
from webserver.resource.logger import app_logger
from config.loggerconfig import LoggerConfig

urls = (
    '/', 'Index',
    '/camera', app_camera,
    '/image', app_image,
    '/start', app_start,
    '/logger', app_logger
)

app = web.application(urls, globals())


class Index:
    def GET(self):
        web.header('Content-type', 'text/html')
        return "Hello, world!"


if __name__ == "__main__":
    logging.basicConfig(
        filename=LoggerConfig().FILE_PATH,
        level=LoggerConfig().level,
        format=LoggerConfig().FORMAT,
        datefmt=LoggerConfig().DATE_FORMAT
    )
    app.run()