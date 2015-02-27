from detection.Detection import *

print("Detection starten")

detection = Detection()
detectionConfig = DetectionConfig()
detectionConfig.contrast = 100
detectionConfig.greyscale = False
detectionConfig.lineY = 720
detection.detect(detectionConfig)
