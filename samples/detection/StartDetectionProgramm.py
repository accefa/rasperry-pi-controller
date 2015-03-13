from detection.detection import Detection
from detection.detectionconfig import DetectionConfig

print("Detection starten")

detection = Detection()
detectionConfig = DetectionConfig()
detectionConfig.contrast = 100
detectionConfig.greyscale = True
detectionConfig.line_y = 1500
detectionConfig.line_h = 300
detectionConfig.crop_x = 1500
detectionConfig.image_path = '../../runtime/detected.jpg'
detectionConfig.greyscale_threshold=28
detection.detect(detectionConfig)
