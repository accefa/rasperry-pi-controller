from PIL import Image
#from picamera import PiCamera

class Detection(object):
    def detect(self):
        #picam = PiCamera()
        #picam.resolution = (1280, 720)
        #picam.exposure_compensation = 2
        #picam.exposure_mode = 'spotlight'
        #picam.meter_mode = 'matrix'
        #picam.image_effect = 'gpen' 
        # Give the camera some time to adjust to conditions
        #picam.sleep(2)
        #picam.capture('foo.jpg')
        
        # 1. PICamera verwenden und Parameter setzen
        # 2. PICamera foto machen
        # 3. PICamera Foto in PIL laden
        # 4. PICamera PIL Image Verarbeitung
        # 5. Foto irgendwo hinspeichern
        return False

class DetectionConfig(object):
    def __init__(self): 
        self.quality = 100
        self.roiX = 0
        self.roiY = 0
        self.roiH = 0
        self.roiW = 0
        self.contrast = 0
        self.greyscale = True
        self.lineH = 0
        self.lineY = 5
    
    @property
    def lineH(self):
        return self.__lineH
    
    @lineH.setter
    def lineH(self, lineH):
        self.__lineH = lineH
    
    @property
    def greyscale(self):
        return self.__greyscale
    
    @greyscale.setter
    def greyscale(self, greyscale):
        self.__greyscale = greyscale
    
    @property
    def contrast(self):
        return self.__contrast
    
    @contrast.setter
    def contrast(self, contrast):
        self.__contrast = contrast
    
    @property
    def roiW(self):
        return self.__roiW
    
    @roiW.setter
    def roiW(self, roiW):
        self.__roiW = roiW
    
    @property
    def roiH(self):
        return self.__roiH
    
    @roiH.setter
    def roiH(self, roiH):
        self.__roiH = roiH
    
    @property
    def roiY(self):
        return self.__roiY
    
    @roiY.setter
    def roiY(self, roiY):
        self.__roiX = roiY
    
    @property
    def roiX(self):
        return self.__roiX
    
    @roiX.setter
    def roiX(self, roiX):
        self.__roiX = roiX
    
    @property
    def quality(self):
        return self.__quality
    
    @quality.setter
    def quality(self, quality):
        self.__quality = quality
    
    @property
    def lineY(self):
        return self.__lineY
    
    @lineY.setter
    def lineY(self, lineY):
        self.__lineY = lineY