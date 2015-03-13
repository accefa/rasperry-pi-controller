from detection.detection import Detection
from config.detectionconfig import DetectionConfig

print("Detection starten")

detection = Detection()
detectionConfig = DetectionConfig()
detectionConfig.contrast = 100
detectionConfig.greyscale = True
detectionConfig.line_y = 1000
detectionConfig.line_h = 20
detectionConfig.crop_x = 4000
detectionConfig.image_path = '../../runtime/detected.jpg'
detectionConfig.greyscale_threshold=28
detection.detect(detectionConfig)
