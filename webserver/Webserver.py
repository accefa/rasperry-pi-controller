import web;

urls = (
  '/', 'index',
  '/camera', 'camera',
  '/image', 'image',
  '/start', 'start'
)

class index:
    def GET(self):
        return "Hello, world!"
    
class camera:
    def GET(self):
        return "GET Camera"
    
    def PUT(self):
        return "PUT Camera"
    
class image:
    def GET(self):
        return "GET Image"
    
class start:
    def GET(self):
        return "GET Start"
    
    def PUT(self):
        return "PUT Start"
    
if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()  
