import os
import platform
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import logging

# Detektions-Klasse. Interagiert mit der Kamera.
class Detection(object):
    def detect(self, detectConfig):
        
        logging.debug("Starte Detektierung")

        if platform.system() == 'Linux':
            shoot = __import__('detection.Camera', fromlist=['shoot']).shoot
            image = shoot(detectConfig)
        else:
            image = Image.open(os.path.dirname(__file__) + "/../images/greyscaleandcontrast_quality50_17_40.jpg")

        image_processor = ImageProcessor(image, detectConfig)
        image_processor.process_image()


class ImageProcessor(object):
    def __init__(self, image, detectConfig):
        self.image = image
        self.detectConfig = detectConfig

    def COLOR_RED(self):
        return (255, 0, 0, 0)

    def COLOR_YELLOW(self):
        return (255, 255, 0, 0)

    def crop_image(self):
        cropx = self.detectConfig.crop_x
        if self.getImageWidth() > (2 * cropx):
            left = cropx
            top = 0
            width = self.getImageWidth() - left
            height = self.getImageHeight() - top
            box = (left, top, width, height)
            self.image = self.image.crop((box))
        else:
            logging.warning('Kein seitlicher Zuschnitt. Cropx ist mit ' + str(cropx) + ' gross. Bild ist nur ' + str(self.getImageWidth()) + ' breit.')
            # TODO warning
        

    def process_image(self):
        self.crop_image()
        xPoint = self.analyzeLine(self.detectConfig.line_y, self.detectConfig.line_h)
        self.drawAngle(180)  # TODO Pass correct angle
        self.drawCrosshairs(xPoint, self.detectConfig.line_y)
        self.saveImage()

    def analyzeLine(self, yPos, rangeHeight):
        if yPos > self.getImageHeight():
            logging.warning('Keine Analyse. Y-Position ist mit ' + str(yPos) + ' zu gross. Bild ist nur ' + str(self.getImageHeight()) + ' gross.')
            return 0
        
        if self.getImageHeight() < (rangeHeight * 2):
            logging.warning('Keine Analyse. Y-Analyse Band ist mit ' + str(rangeHeight) + ' zu gross. Bild ist nur ' + str(self.getImageHeight()) + ' gross.')
            return 0
        
        sectionCalculator = SectionCalculator()
        
        start = yPos - rangeHeight
        if start < 0:
            start = 0

        end = yPos + rangeHeight
        if end > self.getImageHeight():
            end = self.getImageHeight()
            
        for y in range(start, end):
            analizedLine = LineAnalyzing(y, self.detectConfig.greyscale_threshold)
            for x in range(0, self.getImageWidth()):
                xy = (x, y)
                rgb = self.image.getpixel(xy)
                rgbPoint = RgbPoint(x, y, rgb)
                analizedLine.addPoint(rgbPoint)
            analizedLine.analyze()
            if analizedLine.hasSection():
                self.drawLine(analizedLine.getFirstPoint().x, analizedLine.getFirstPoint().y, analizedLine.getLastPoint().x,
                              analizedLine.getLastPoint().y)
                sectionCalculator.addSection(analizedLine.getLongestSection())
        return sectionCalculator.getAverageX()

    def drawLine(self, xStart, yStart, xEnd, yEnd):
        draw = ImageDraw.Draw(self.image)
        draw.line((xStart, yStart, xEnd, yEnd), fill=self.COLOR_RED(), width=1)

    def drawAngle(self, angle):
        font = ImageFont.truetype(os.path.dirname(os.path.realpath(__file__)) + "/../config/Arial.ttf", 100)
        draw = ImageDraw.Draw(self.image)
        x = self.getImageWidth() - 180
        y = self.getImageHeight() - 110
        draw.text((x, y), str(angle), font=font, fill=self.COLOR_RED())

    def drawCrosshairs(self, pointX, pointY):
        length = 50
        crosshairsThickness = 10
        crosshairsColor = self.COLOR_YELLOW()
        draw = ImageDraw.Draw(self.image)
        draw.line((pointX, pointY, pointX, pointY + length), fill=crosshairsColor, width=crosshairsThickness)
        draw.line((pointX, pointY, pointX, pointY - length), fill=crosshairsColor, width=crosshairsThickness)
        draw.line((pointX, pointY, pointX + length, pointY), fill=crosshairsColor, width=crosshairsThickness)
        draw.line((pointX, pointY, pointX - length, pointY), fill=crosshairsColor, width=crosshairsThickness)

    def saveImage(self):
        self.image.save(self.detectConfig.image_path)

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
        return self.calculateAvg(xValues)

    def calculateAvg(self, values):
        if not isinstance(values, list):
            return 0
        summe = 0
        for value in values:
            summe += value
        if summe == 0:
            return 0
        avg = summe / len(values)
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

    def hasSection(self):
        return len(self.sections) != 0

    def getLongestSection(self):
        if not self.hasSection():
            return None
        
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
        if longestSection is None:
            return Point(0, 0)
        return Point(longestSection.xStart, self.y)

    def getLastPoint(self):
        longestSection = self.getLongestSection()
        if longestSection is None:
            return Point(0, 0)
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
    def __init__(self, x, y):
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
    def __init__(self, x, y, rgb):
        Point.__init__(self, x, y)
        self.rgb = rgb

    @property
    def rgb(self):
        return self.__rgb

    @rgb.setter
    def rgb(self, rgb):
        self.__rgb = rgb