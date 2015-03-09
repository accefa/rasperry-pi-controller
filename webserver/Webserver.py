import web
from webserver.resource.camera import app_camera

urls = (
  '/', 'index',
  '/camera', app_camera,
  '/image', 'image',
  '/start', 'start'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        web.header('Content-type', 'text/html') 
        return "Hello, world!"

class image:
    def GET(self):
        return "GET Image"

class start:
    def GET(self):
        return "GET Start"
    
    def PUT(self):
        return "PUT Start"
    
if __name__ == "__main__": 
    app.run()  
