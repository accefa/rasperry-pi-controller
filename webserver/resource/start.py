import json
import web
from detection.detection import Detection
from config.detectionconfig import DetectionConfig


urls = (
    "(.*)", "Start"
)

app_start = web.application(urls, locals())

CALLBACK_URL_KEY = 'url'


class Start:
    def PUT(self, path):
        try:
            request_dict = json.loads(web.data())

            if CALLBACK_URL_KEY in request_dict:
                callback_url = request_dict[CALLBACK_URL_KEY]
            else:
                raise ValueError('No url key found')

			# TODO Standort ermitteln
            config = DetectionConfig()
            Detection().detect(config)

			# TODO X-Koordiante auf Anzahl Schritte ummappen
			
			# TODO Stepper Schritte delegieren
			
			# TODO Rad anwerfen
			
			# TODO Starten mit Ballnachschub
			
			# TODO Alle Motoren abschalten und zurücksetzen
			
			# TODO Callback oder Prozess einfach beenden
			
            web.header('Content-type', 'text/json')
            web.ok()
            return callback_url
        except (TypeError, ValueError) as e:
            web.header('Content-type', 'text/html')
            web.notacceptable()
            return e.message
