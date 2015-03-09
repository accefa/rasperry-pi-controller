import web


urls = (
    "(.*)", "Start"
)

app_start = web.application(urls, locals())


class Start:
    def GET(self, path):
        web.header('Content-type', 'text/html')
        return "GET Start"

    def PUT(self, path):
        web.header('Content-type', 'text/html')
        return "PUT Start"