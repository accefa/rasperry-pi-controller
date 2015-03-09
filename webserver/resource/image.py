import web

urls = (
    "(.*)", "image"
)

app_image = web.application(urls, locals())

class image:
    def GET(self, path):
        web.header('Content-type', 'text/html')
        return "GET Image"