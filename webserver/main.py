import web
from webserver.resource.camera import app_camera
from webserver.resource.image import app_image

urls = (
  '/', 'index',
  '/camera', app_camera,
  '/image', app_image,
  '/start', 'start'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        web.header('Content-type', 'text/html') 
        return "Hello, world!"

class start:
    def GET(self):
        return "GET Start"
    
    def PUT(self):
        return "PUT Start"
    
if __name__ == "__main__": 
    app.run()  
