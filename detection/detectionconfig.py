# coding=utf-8
# Daten-Objekt. Enthält alle Konfigurations-Einstellungen für die Detektierung.


class DetectionConfig(object):
    QUALITY_KEY = 'quality'
    CROP_X_KEY = 'crop_x'
    CONTRAST_KEY = 'contrast'
    GREYSCALE_KEY = 'greyscale'
    GREYSCALE_THRESHOLD_KEY = 'greyscale_threshold'
    LINE_H_KEY = 'line_h'
    LINE_Y_KEY = 'line_y'
    IMAGE_PATH_KEY = 'image_path'

    def __init__(self):
        self.quality = 100
        self.crop_x = 0
        self.contrast = 0
        self.greyscale = True
        self.greyscale_threshold = 30
        self.line_h = 0
        self.line_y = 5
        self.image_path = "/tmp/image.jpg"

    def set_from_dict(self, dict):
        if self.QUALITY_KEY in dict:
            self.quality = dict[self.QUALITY_KEY]

        if self.CROP_X_KEY in dict:
            self.crop_x = dict[self.CROP_X_KEY]

        if self.CONTRAST_KEY in dict:
            self.contrast = dict[self.CONTRAST_KEY]

        if self.GREYSCALE_KEY in dict:
            self.greyscale = dict[self.GREYSCALE_KEY]

        if self.GREYSCALE_THRESHOLD_KEY in dict:
            self.greyscale_threshold = dict[self.GREYSCALE_THRESHOLD_KEY]

        if self.LINE_H_KEY in dict:
            self.line_h = dict[self.LINE_H_KEY]

        if self.LINE_Y_KEY in dict:
            self.line_y = dict[self.LINE_Y_KEY]

        if self.IMAGE_PATH_KEY in dict:
            self.image_path = dict[self.IMAGE_PATH_KEY]

    def get_as_dict(self):
        return {
            self.QUALITY_KEY: self.quality,
            self.CROP_X_KEY: self.crop_x,
            self.CONTRAST_KEY: self.contrast,
            self.GREYSCALE_KEY: self.greyscale,
            self.GREYSCALE_THRESHOLD_KEY: self.greyscale_threshold,
            self.LINE_H_KEY: self.line_h,
            self.LINE_Y_KEY: self.line_y,
            self.IMAGE_PATH_KEY: self.image_path
        }

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
    def crop_x(self):
        return self.__crop_x

    @crop_x.setter
    def crop_x(self, crop_x):
        if crop_x < 0:
            crop_x = 0
        self.__crop_x = crop_x

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
    def greyscale(self):
        return self.__greyscale

    @greyscale.setter
    def greyscale(self, greyscale):
        if not (isinstance(greyscale, (bool))):
            greyscale = False
        self.__greyscale = greyscale

    @property
    def greyscale_threshold(self):
        return self.__greyscaleThreshold

    @greyscale_threshold.setter
    def greyscale_threshold(self, greyscale_threshold):
        if greyscale_threshold > 255:
            greyscale_threshold = 255
        elif greyscale_threshold < 0:
            greyscale_threshold = 0
        self.__greyscaleThreshold = greyscale_threshold

    @property
    def line_h(self):
        return self.__line_h

    @line_h.setter
    def line_h(self, line_h):
        if line_h < 1:
            line_h = 1
        self.__line_h = line_h

    @property
    def line_y(self):
        return self.__line_y

    @line_y.setter
    def line_y(self, line_y):
        if line_y < 0:
            line_y = 0
        self.__line_y = line_y

    @property
    def image_path(self):
        return self.__image_path

    @image_path.setter
    def image_path(self, image_path):
        self.__image_path = image_path