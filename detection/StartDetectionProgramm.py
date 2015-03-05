from detection.Detection import *

print("Detection starten")

detection = Detection()
detectionConfig = DetectionConfig()
detectionConfig.contrast = 100
detectionConfig.greyscale = True
detectionConfig.lineY = 1000
detectionConfig.lineH = 275
detectionConfig.pathSaveImageTo = 'test.jpg'
detectionConfig.greyscaleThreshold=28
detection.detect(detectionConfig)
