import web

urls = (
    "(.*)", "Image"
)

app_image = web.application(urls, locals())


class Image:
    def GET(self, path):
        web.header('Content-type', 'text/html')
        return "GET Image"