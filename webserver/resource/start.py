import json
import web
import platform
from detection.detection import Detection
from config.detectionconfig import DetectionConfig


urls = (
    "(.*)", "Start"
)

app_start = web.application(urls, locals())

CALLBACK_URL_KEY = 'url'

class Start:
    def PUT(self, path):
         print("Serielle Schnittstellen laden")
         stp_serial = get_stp_serial()
         bldc_serial = get_bldc_serial()
         dc_serial = get_dc_serial()
         
         print("Reset der Motoren")
         stp_serial.reset()
         bldc_serial.reset()
         dc_serial.reset()
         
         print("Bild erkennen")
         config = DetectionConfig()
         steps = Detection().detect(config)
         
         print("Stepper rangieren. Schritte: " + str(steps))
         stp_serial.start(steps)

         rpm = 8000;
         print("Schwungrad in Kampfmodus setzen mit RPM: " + str(rpm))
         bldc_serial.start(rpm)

         print("Ballnachschub starten")
         dc_serial.forward()
         
         print("Motoren abschalten")
         bldc_serial.stop()
         
         web.header('Content-type', 'text/json')
         web.ok()
         return 'done'

def get_stp_serial():
    stp_serial_class_name = 'StpSerial'
    stp_serial_base_module = 'piserial.stp'
    if platform.system() == 'Linux':
        stp_serial_module = __import__(stp_serial_base_module + '.' + 'stp_serial', fromlist=[stp_serial_class_name])
    else:
        stp_serial_module = __import__(stp_serial_base_module + '.' + 'stp_stub', fromlist=[stp_serial_class_name])
    return getattr(stp_serial_module, stp_serial_class_name)

def get_bldc_serial():
    bldc_serial_class_name = 'BldcSerial'
    bldc_serial_base_module = 'piserial.bldc'
    if platform.system() == 'Linux':
        bldc_serial_module = __import__(bldc_serial_base_module + '.' + 'bldc_serial',
                                        fromlist=[bldc_serial_class_name])
    else:
        bldc_serial_module = __import__(bldc_serial_base_module + '.' + 'bldc_stub', fromlist=[bldc_serial_class_name])
    return getattr(bldc_serial_module, bldc_serial_class_name)

def get_dc_serial():
    dc_serial_class_name = 'DcSerial'
    dc_serial_base_module = 'piserial.dc'
    if platform.system() == 'Linux':
        dc_serial_module = __import__(dc_serial_base_module + '.' + 'dc_serial', fromlist=[dc_serial_class_name])
    else:
        dc_serial_module = __import__(dc_serial_base_module + '.' + 'dc_stub', fromlist=[dc_serial_class_name])
    return getattr(dc_serial_module, dc_serial_class_name)