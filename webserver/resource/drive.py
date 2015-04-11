import web
from webserver.resource.bldc import app_drive_bldc
from webserver.resource.dc import app_drive_dc
from webserver.resource.stp import app_drive_stp


urls = (
    '/bldc', app_drive_bldc,
    '/dc', app_drive_dc,
    '/stp', app_drive_stp
)

app_drive = web.application(urls, locals())
