# coding=utf-8
# Daten-Objekt. Enthält alle Konfigurations-Einstellungen für die Detektierung.


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
        if not (isinstance(greyscale, (bool))):
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