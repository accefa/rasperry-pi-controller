from detection.Detection import *

print("Detection starten")

detection = Detection()
detectionConfig = DetectionConfig()
detectionConfig.contrast = 100
detectionConfig.greyscale = True
detectionConfig.lineY = 950
detectionConfig.lineH = 40
detectionConfig.greyscaleThreshold=30
detection.detect(detectionConfig)
