import web;
import json;

urls = (
  '/', 'index',
  '/camera', 'camera',
  '/image', 'image',
  '/start', 'start'
)

app = web.application(urls, globals())

CONFIG_FILE_PATH = 'config.json'

class index:
    def GET(self):
        web.header('Content-type', 'text/html') 
        return "Hello, world!"
    
class camera:
    def GET(self):
        try:            
            with open(CONFIG_FILE_PATH) as configFile:
                config = json.load(configFile)
            
            web.header('Content-type', 'text/json')
            web.accepted
            return json.dumps(config)
        except (TypeError, ValueError) as e:
            web.internalerror()
            web.header('Content-type', 'text/json')
    
    def PUT(self):
        try:
            jsonData = web.data()
            config = json.loads(jsonData)
            
            with open(CONFIG_FILE_PATH, 'w') as f:
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
