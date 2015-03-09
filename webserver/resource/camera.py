import json

import web


urls = (
    "(.*)", "camera"
)

CONFIG_FILE_PATH = 'config.json'

class camera:
    def GET(self, path):
        try:            
            with open(CONFIG_FILE_PATH) as configFile:
                config = json.load(configFile)
            
            web.header('Content-type', 'text/json')
            web.ok()
            return json.dumps(config)
        except (TypeError, ValueError) as e:
            print e.message
            web.header('Content-type', 'text/json')
            web.internalerror()
    
    def PUT(self, path):
        try:
            jsonData = web.data()
            config = json.loads(jsonData)
            
            with open(CONFIG_FILE_PATH, 'w') as f:
                json.dump(config, f)
            
            web.header('Content-type', 'text/json')
            web.ok()
        except (TypeError, ValueError) as e:
            print e.message
            web.header('Content-type', 'text/json')
            web.notacceptable()
            
app_camera = web.application(urls, locals())

if __name__ == "__main__": 
    app_camera.run()  