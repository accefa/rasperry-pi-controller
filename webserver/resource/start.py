import json
import web
import platform
import logging
import time
from detection.detection import Detection
from config.detectionconfig import DetectionConfig


urls = (
    "(.*)", "Start"
)

app_start = web.application(urls, locals())

# Mit Ervin abgesprochen
# BLDC ON, BLDC SETRPM 10000, STP RESET, STP MOVE XY, DC UP, DC ON, BLDC OFF

class Start:
    def PUT(self, path):
         try:
             logging.info("Korb erkennen")
             config = DetectionConfig()
             steps = Detection().detect(config)
             steps = (-1) * steps;
             
             logging.info("Serielle Schnittstellen laden")
             stp_serial = get_stp_serial()
             bldc_serial = get_bldc_serial()
             dc_serial = get_dc_serial()
             
             rpm = 6250; # TODO Optimaler Wert?
             logging.info("Schwungrad in Kampfmodus setzen mit RPM: " + str(rpm))
             bldc_serial.start(rpm)
             
             logging.info("Ballnachschub reseten")
             stp_serial.reset() # koennte man in einrichtungsphase machen.
             
             logging.info("Stepper rangieren. Schritte: " + str(steps))
             stp_serial.start(steps)
             
             logging.info("Ballnachschub starten")
             dc_serial.forward()

             time.sleep(9) # TODO Optimaler Wert

             logging.info("Motoren abschalten")
             bldc_serial.stop()

             web.header('Content-type', 'text/plain')
             web.ok()
             return 'done'
         except (TypeError, ValueError) as e:
            web.header('Content-type', 'text/html')
            web.internalerror()
            return e.message

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