import json

import web


urls = (
    "(.*)", "start"
)

app_start = web.application(urls, locals())


class start:
    def GET(self, path):
        web.header('Content-type', 'text/html')
        return "GET Start"

    def PUT(self, path):
        web.header('Content-type', 'text/html')
        return "PUT Start"