import web;
import json;

urls = (
  '/', 'index',
  '/camera', 'camera',
  '/image', 'image',
  '/start', 'start'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        web.header('Content-type', 'text/html') 
        return "Hello, world!"
    
class camera:
    def GET(self):
        return "GET Camera"
    
    def PUT(self):
        try:
            jsonData = web.data()
            config = json.loads(jsonData)
            
            with open('config.json', 'w') as f:
                json.dump(config, f)
            
            web.header('Content-type', 'text/json')
            web.accepted
        except (TypeError, ValueError) as e:
            web.notacceptable()
            web.header('Content-type', 'text/json')
    
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
