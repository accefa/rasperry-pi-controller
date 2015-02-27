from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class Detection(object):
    def detect(self, detectConfig):
        imageProcessor = ImageProcessor("greyscaleandcontrast_quality50_17_40.jpg", detectConfig)
        imageProcessor.processImage()
        return False

class ImageProcessor(object):
    def __init__(self, sourceImagePath, detectConfig): 
        self.sourceImagePath = sourceImagePath
        self.detectConfig = detectConfig
    
    def processImage(self):
        self.image = Image.open(self.sourceImagePath)
        self.analyzeLine(self.detectConfig.lineY)
        self.drawAngle(50)
        self.drawCrosshairs(200, 200)
        self.showImage()
        
    def analyzeLine(self, y):
        imageWidth = self.image.size[0]
        threshold = 30
        for x in range(0, imageWidth):
            xy = (x, y)
            rgb = self.image.getpixel(xy)
            if(rgb[0] < threshold):
                self.image.putpixel(xy, (128,256,0))
    
    def drawAngle(self, angle):
        font = ImageFont.truetype("Arial.ttf",100)
        draw = ImageDraw.Draw(self.image)
        draw.text((0,0), str(angle) + " G.", font=font, fill=(255,0,0,0))
    
    def drawCrosshairs(self, pointX, pointY):
        length = 40
        draw = ImageDraw.Draw(self.image)
        draw.line((pointX, pointY + length, pointX, pointY), fill=(255,0,0,0), width=5)
        draw.line((pointX, pointY - length, pointX, pointY), fill=(255,0,0,0), width=5)
        draw.line((pointX, pointY, pointX + length, pointY), fill=(255,0,0,0), width=5)
        draw.line((pointX, pointY, pointX - length, pointY), fill=(255,0,0,0), width=5)
        
    def saveImage(self, path):
        self.image.save(path)   
    
    def showImage(self):
        self.image.show()
        
    @property
    def sourceImagePath(self):
        return self.__sourceImagePath
    
    @sourceImagePath.setter
    def sourceImagePath(self, sourceImagePath):
        self.__sourceImagePath = sourceImagePath
    
    @property
    def detectConfig(self):
        return self.__detectConfig
    
    @detectConfig.setter
    def detectConfig(self, detectConfig):
        self.__detectConfig = detectConfig
    
    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, image):
        self.__image = image

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
        self.pathSaveImageTo = "/tmp/image.jpg"
    
    @property
    def pathSaveImageTo(self):
        return self.__pathSaveImageTo
    
    @pathSaveImageTo.setter
    def pathSaveImageTo(self, pathSaveImageTo):
        self.__pathSaveImageTo = pathSaveImageTo
    
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
        if quality > 100:
            quality = 100
        elif quality < 0:
            quality = 0
        self.__quality = quality
    
    @property
    def lineY(self):
        return self.__lineY
    
    @lineY.setter
    def lineY(self, lineY):
        self.__lineY = lineY