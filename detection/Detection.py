from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
# from Camera import CameraController

# Detektions-Klasse. Interagiert mit der Kamera.
class Detection(object):
    def detect(self, detectConfig):
        image = Image.open("greyscaleandcontrast_quality50_17_40.jpg")
        # cameraController = CameraController()
        # image = cameraController.shoot(detectConfig)
        imageProcessor = ImageProcessor(image, detectConfig)
        imageProcessor.processImage()
        return False

class ImageProcessor(object):
    def __init__(self, image, detectConfig): 
        self.image = image
        self.detectConfig = detectConfig

    def COLOR_RED(self):
        return (255,0,0,0)
    
    def COLOR_YELLOW(self):
        return (255,255,0,0)
    
    def cropImage(self):
        cropX = self.detectConfig.cropX
        left = cropX
        top = 0
        width = self.getImageWidth() - cropX
        height = self.getImageHeight()
        box = (left, top, width, height)
        self.image = self.image.crop((box))
    
    def processImage(self):
        self.cropImage()
        xPoint = self.analyzeLine(self.detectConfig.lineY, self.detectConfig.lineH)
        self.drawAngle(180) # TODO Pass correct angle
        self.drawCrosshairs(xPoint, self.detectConfig.lineY)
        #self.showImage() # instead of show, save
        self.saveImage()

    def analyzeLine(self, yPos, rangeHeight):
        sectionCalculator = SectionCalculator()
        start = yPos - rangeHeight
        end = yPos + rangeHeight
        for y in range(start, end):
            analizedLine = LineAnalyzing(y, self.detectConfig.greyscaleThreshold)
            for x in range(0, self.getImageWidth()):
                xy = (x, y)
                rgb = self.image.getpixel(xy)
                rgbPoint = RgbPoint(x, y, rgb)
                analizedLine.addPoint(rgbPoint)
            analizedLine.analyze()
            self.drawLine(analizedLine.getFirstPoint().x, analizedLine.getFirstPoint().y, analizedLine.getLastPoint().x, analizedLine.getLastPoint().y)
            sectionCalculator.addSection(analizedLine.getLongestSection())
        
        return sectionCalculator.getAverageX()
        
    def drawLine(self, xStart, yStart, xEnd, yEnd):
        draw = ImageDraw.Draw(self.image)
        draw.line((xStart, yStart, xEnd, yEnd), fill=self.COLOR_RED(), width=1)
        
    def drawAngle(self, angle):
        font = ImageFont.truetype("Arial.ttf", 100)
        draw = ImageDraw.Draw(self.image)
        x = self.getImageWidth() - 180
        y = self.getImageHeight() - 110
        draw.text((x,y), str(angle), font=font, fill=self.COLOR_RED())
    
    def drawCrosshairs(self, pointX, pointY):
        length = 50
        crosshairsThickness = 10
        crosshairsColor = self.COLOR_YELLOW()
        draw = ImageDraw.Draw(self.image)
        draw.line((pointX, pointY + length, pointX, pointY), fill=crosshairsColor, width=crosshairsThickness)
        draw.line((pointX, pointY - length, pointX, pointY), fill=crosshairsColor, width=crosshairsThickness)
        draw.line((pointX, pointY, pointX + length, pointY), fill=crosshairsColor, width=crosshairsThickness)
        draw.line((pointX, pointY, pointX - length, pointY), fill=crosshairsColor, width=crosshairsThickness)
        
    def saveImage(self):
        self.image.save(self.detectConfig.pathSaveImageTo)   
    
    def showImage(self):
        self.image.show()
        
    def getImageWidth(self):
        return self.image.size[0]
    
    def getImageHeight(self):
        return self.image.size[1]
        
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


class SectionCalculator(object):
    def __init__(self): 
        self.sections = []
        
    def addSection(self, section):
        if isinstance(section, LineSection):
            self.sections.append(section)
        else:
            raise Exception("addSection does only support LineSection")
        
    def getAverageX(self):
        xValues = []
        for section in self.sections:
            diff = section.xEnd - section.xStart
            xValues.append(section.xEnd - (diff / 2))
        avg = reduce(lambda x, y: x + y, xValues) / len(xValues)
        return avg

class LineAnalyzing(object):
    def __init__(self, y, greyscaleThreshold): 
        self.y = y
        self.line = []
        self.sections = []
        self.greyscaleThreshold = greyscaleThreshold
        
    def addPoint(self, rgbPoint):
        if isinstance(rgbPoint, RgbPoint):
            self.line.append(rgbPoint)
        else:
            raise Exception("addPoint does only support RgbPoint")

    def analyze(self):
        self.eliminiatePointsOverThreshold()
        self.createSections()
    
    def getLongestSection(self):
        longestSection = self.sections[0]
        for section in self.sections:
            if longestSection.getWidth() < section.getWidth():
                longestSection = section
        return longestSection
    
    def eliminiatePointsOverThreshold(self):
        newLine = []
        for rgbPoint in self.line:
            if (rgbPoint.rgb[0] <= self.greyscaleThreshold):
                newLine.append(rgbPoint)
        self.line = newLine
        
    def createSections(self):
        sections = []

        if len(self.line) == 0:
            self.sections = sections
            return

        goToNextPoint = False
        tmpPoint = self.line[0]
        for index, currentPoint in enumerate(self.line):
            if goToNextPoint:
                tmpPoint = currentPoint
                goToNextPoint = False
                
            if (len(self.line) == index + 1):
                # am ende der linie
                sections.append(LineSection(self.y, tmpPoint.x, currentPoint.x))
            elif currentPoint.x != (self.line[index + 1].x - 1):
                sections.append(LineSection(self.y, tmpPoint.x, currentPoint.x))
                goToNextPoint = True
                
        self.sections = sections
        
    def getFirstPoint(self):
        longestSection = self.getLongestSection()
        return Point(longestSection.xStart, self.y)
        
    def getLastPoint(self):
        longestSection = self.getLongestSection()
        return Point(longestSection.xEnd, self.y)

# Daten-Objekt. Eine einzelne Line-Sektion.
class LineSection(object):
    def __init__(self, y, xStart, xEnd):
        self.y = y
        self.xStart = xStart
        self.xEnd = xEnd
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        if y < 0:
            y = 0
        self.__y = y
        
    @property
    def xStart(self):
        return self.__xStart
    
    @xStart.setter
    def xStart(self, xStart):
        if xStart < 0:
            xStart = 0
        self.__xStart = xStart
    
    @property
    def xEnd(self):
        return self.__xEnd
    
    @xEnd.setter
    def xEnd(self, xEnd):
        if xEnd < 0:
            xEnd = 0
        self.__xEnd = xEnd
    
    def getWidth(self):
        return self.xEnd - self.xStart

# Datenobjekt. Ein Pixel.
class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        if x < 0:
            x = 0
        self.__x = x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        if y < 0:
            y = 0
        self.__y = y
        
# Daten-Objekt. RGB-Punkt mit Positionswerten.
class RgbPoint(Point):
    def __init__(self,x,y,rgb):
        Point.__init__(self, x, y)
        self.rgb = rgb
    
    @property
    def rgb(self):
        return self.__rgb
    
    @rgb.setter
    def rgb(self, rgb):
        self.__rgb = rgb
    
# Daten-Objekt. Enthaelt alle Konfigurations-Einstellungen 
# fuer die Detektierung.
class DetectionConfig(object):
    def __init__(self): 
        self.quality = 100
        self.cropX = 0
        self.contrast = 0
        self.greyscale = True
        self.lineH = 0
        self.lineY = 5
        self.pathSaveImageTo = "/tmp/image.jpg"
        self.greyscaleThreshold = 30
    
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
        if lineH < 1:
            lineH = 1
        self.__lineH = lineH
    
    @property
    def greyscale(self):
        return self.__greyscale
    
    @greyscale.setter
    def greyscale(self, greyscale):
        if not(isinstance(greyscale, (bool))):
            greyscale = False
        self.__greyscale = greyscale
    
    @property
    def contrast(self):
        return self.__contrast
    
    @contrast.setter
    def contrast(self, contrast):
        if contrast > 100:
            contrast = 100
        elif contrast < -100:
            contrast = -100
        self.__contrast = contrast
    
    @property
    def cropX(self):
        return self.__cropX
    
    @cropX.setter
    def cropX(self, cropX):
        if cropX < 0:
            cropX = 0
        self.__cropX = cropX
        
    @property
    def greyscaleThreshold(self):
        return self.__greyscaleThreshold
    
    @greyscaleThreshold.setter
    def greyscaleThreshold(self, greyscaleThreshold):
        if greyscaleThreshold > 255:
            greyscaleThreshold = 255
        elif greyscaleThreshold < 0:
            greyscaleThreshold = 0
        self.__greyscaleThreshold = greyscaleThreshold
    
    @property
    def quality(self):
        return self.__quality
    
    @quality.setter
    def quality(self, quality):
        if quality > 100:
            quality = 100
        elif quality < 1:
            quality = 1
        self.__quality = quality
    
    @property
    def lineY(self):
        return self.__lineY
    
    @lineY.setter
    def lineY(self, lineY):
        if lineY < 0:
            lineY = 0
        self.__lineY = lineY