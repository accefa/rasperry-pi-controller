import json

import web

from config.loggerconfig import LoggerConfig


urls = (
    "(.*)", "Logger"
)

app_logger = web.application(urls, locals())

class Logger:
    def GET(self, path):
        try:
            with open(LoggerConfig().FILE_PATH) as log_file:
                web.header('Content-type', 'text/plain')
                web.ok()
                return log_file.read()
        except (TypeError, ValueError) as e:
            web.header('Content-type', 'text/html')
            web.internalerror()
            return e.message

    def PUT(self, path):
        try:
            config_dict = json.loads(web.data())

            logger_config = LoggerConfig()
            logger_config.set_from_dict(config_dict)

            web.header('Content-type', 'text/json')
            web.ok()
            return json.dumps(logger_config.get_as_dict())
        except (TypeError, ValueError) as e:
            web.header('Content-type', 'text/html')
            web.notacceptable()
            return e.message
