from detection.detection import Detection
from config.detectionconfig import DetectionConfig

print("Detection starten")

detection = Detection()
detectionConfig = DetectionConfig()
detectionConfig.contrast = 100
detectionConfig.greyscale = True
detectionConfig.line_y = 1000
detectionConfig.line_h = 200
detectionConfig.crop_x = 400
detectionConfig.image_path = '../../runtime/detected.jpg'
detectionConfig.greyscale_threshold=28
detection.detect(detectionConfig)
