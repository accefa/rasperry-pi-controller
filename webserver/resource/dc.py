import web

urls = (
    '(.*)/forward', 'Forward',
    '(.*)/backward', 'Backward',
    '(.*)/reset', 'Reset'
)

app_drive_dc = web.application(urls, locals())


class Forward:
    def POST(self, path):
        # TODO Call ET-Interface

        web.header('Content-type', 'text/json')
        web.ok()


class Backward:
    def POST(self, path):
        # TODO Call ET-Interface

        web.header('Content-type', 'text/json')
        web.ok()


class Reset:
    def POST(self, path):
        # TODO Call ET-Interface

        web.header('Content-type', 'text/json')
        web.ok()