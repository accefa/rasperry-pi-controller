#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET

tree = ET.parse('user_data.xml')
root = tree.getroot()

urls = (
    '/', 'start',
    '/users', 'list_users',
    '/users/(.*)', 'get_user'
)

class start:
    def GET(self):
        return 'The Process is starting. Please wait while Wuethrich is going to take a coffee for you.'

class list_users:        
    def GET(self):
        output = 'users:[';
        for child in root:
                print 'child', child.tag, child.attrib
                output += str(child.attrib) + ','
                output += ']';
                return output

class get_user:
    def GET(self, user):
        for child in root:
            if child.attrib['id'] == user:
                return str(child.attrib)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()