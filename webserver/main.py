import web
from webserver.resource.camera import app_camera
from webserver.resource.image import app_image
from webserver.resource.start import app_start

urls = (
  '/', 'index',
  '/camera', app_camera,
  '/image', app_image,
  '/start', app_start
)

app = web.application(urls, globals())

class index:
    def GET(self):
        web.header('Content-type', 'text/html') 
        return "Hello, world!"
    
if __name__ == "__main__": 
    app.run()  
