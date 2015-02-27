class Detection(object): 
    def __init__(self): 
        self._quality = 100
        self._roiX = 0
        self._roiY = 0
        self._roiH = 0
        self._roiW = 0
        self._contrast = 0
        self._greyscale = 0
        self._lineH = 0
        self._lineY = 0

    def setQuality(self, quality):
        self._quality = quality
        
    def getQuality(self):
        return self._quality
    
    def setRoiX(self, roiX):
        self._roiX = roiX
        
    def getRoiX(self):
        return self._roiX