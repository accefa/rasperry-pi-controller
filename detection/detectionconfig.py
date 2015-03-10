# coding=utf-8
# Diese Klasse repräsentiert die Konfiguration welche in der Datei config.json im Hauptverzeichnisses des Projektes
# gespeichert ist. Normalerweise werden die Werte über die Methoden set/get_from_dict oder direkt über die Properties
# bearbeitet. Es ist auch möglich die Datei config.json zu bearbeiten.

import os
import json


class DetectionConfig(object):
    CONFIG_FILE_PATH = os.path.dirname(__file__) + '/../config.json'

    QUALITY_DEFAULT = 90
    QUALITY_KEY = 'quality'
    CROP_X_DEFAULT = 0
    CROP_X_KEY = 'crop_x'
    CONTRAST_DEFAULT = 0
    CONTRAST_KEY = 'contrast'
    GREYSCALE_DEFAULT = True
    GREYSCALE_KEY = 'greyscale'
    GREYSCALE_THRESHOLD_DEFAULT = 0
    GREYSCALE_THRESHOLD_KEY = 'greyscale_threshold'
    LINE_H_DEFAULT = 1
    LINE_H_KEY = 'line_h'
    LINE_Y_DEFAULT = 0
    LINE_Y_KEY = 'line_y'
    IMAGE_PATH_DEFAULT = os.path.dirname(__file__) + '/../images'
    IMAGE_PATH_KEY = 'image_path'

    __default_dict = {
        QUALITY_KEY: QUALITY_DEFAULT,
        CROP_X_KEY: CROP_X_DEFAULT,
        CONTRAST_KEY: CONTRAST_DEFAULT,
        GREYSCALE_KEY: GREYSCALE_DEFAULT,
        GREYSCALE_THRESHOLD_KEY: GREYSCALE_THRESHOLD_DEFAULT,
        LINE_H_KEY: LINE_H_DEFAULT,
        LINE_Y_KEY: LINE_Y_DEFAULT,
        IMAGE_PATH_KEY: IMAGE_PATH_DEFAULT
    }

    __populate_in_progress = False
    __save_in_progress = False

    def __init__(self):
        self.__read()

    def set_from_dict(self, config_dict):
        self.__populate(config_dict)
        self.__save()

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

    def __read(self):
        try:
            config_dict = self.__read_config_from_file()
            self.__populate(config_dict)
        except (TypeError, ValueError) as e:
            config_dict = self.__default_dict
            self.__populate(config_dict)
            self.__save()

    def __read_config_from_file(self):
        with open(self.CONFIG_FILE_PATH) as config_file:
            return json.load(config_file)

    def __populate(self, config_dict):
        self.__populate_in_progress = True

        if self.QUALITY_KEY in config_dict:
            self.quality = config_dict[self.QUALITY_KEY]

        if self.CROP_X_KEY in config_dict:
            self.crop_x = config_dict[self.CROP_X_KEY]

        if self.CONTRAST_KEY in config_dict:
            self.contrast = config_dict[self.CONTRAST_KEY]

        if self.GREYSCALE_KEY in config_dict:
            self.greyscale = config_dict[self.GREYSCALE_KEY]

        if self.GREYSCALE_THRESHOLD_KEY in config_dict:
            self.greyscale_threshold = config_dict[self.GREYSCALE_THRESHOLD_KEY]

        if self.LINE_H_KEY in config_dict:
            self.line_h = config_dict[self.LINE_H_KEY]

        if self.LINE_Y_KEY in config_dict:
            self.line_y = config_dict[self.LINE_Y_KEY]

        if self.IMAGE_PATH_KEY in config_dict:
            self.image_path = config_dict[self.IMAGE_PATH_KEY]

        self.__populate_in_progress = False

    def __save(self):
        if not self.__populate_in_progress:
            self.__save_in_progress = True
            try:
                with open(self.CONFIG_FILE_PATH, 'w') as config_file:
                    json.dump(self.get_as_dict(), config_file, indent=2)
            except (TypeError, ValueError) as e:
                raise e
            finally:
                self.__save_in_progress = False

    # Wenn gespeichert wird nicht mehr lesen sonst Rekursion
    def __read_from_property(self):
        if not self.__save_in_progress:
            self.__read()

    @property
    def quality(self):
        self.__read_from_property()
        return self.__quality

    @quality.setter
    def quality(self, quality):
        if quality > 100:
            quality = 100
        elif quality < 1:
            quality = 1
        self.__quality = quality
        self.__save()

    @property
    def crop_x(self):
        self.__read_from_property()
        return self.__crop_x

    @crop_x.setter
    def crop_x(self, crop_x):
        if crop_x < 0:
            crop_x = 0
        self.__crop_x = crop_x
        self.__save()

    @property
    def contrast(self):
        self.__read_from_property()
        return self.__contrast

    @contrast.setter
    def contrast(self, contrast):
        if contrast > 100:
            contrast = 100
        elif contrast < -100:
            contrast = -100
        self.__contrast = contrast
        self.__save()

    @property
    def greyscale(self):
        self.__read_from_property()
        return self.__greyscale

    @greyscale.setter
    def greyscale(self, greyscale):
        if not (isinstance(greyscale, (bool))):
            greyscale = False
        self.__greyscale = greyscale
        self.__save()

    @property
    def greyscale_threshold(self):
        self.__read_from_property()
        return self.__greyscale_threshold

    @greyscale_threshold.setter
    def greyscale_threshold(self, greyscale_threshold):
        if greyscale_threshold > 255:
            greyscale_threshold = 255
        elif greyscale_threshold < 0:
            greyscale_threshold = 0
        self.__greyscale_threshold = greyscale_threshold
        self.__save()

    @property
    def line_h(self):
        self.__read_from_property()
        return self.__line_h

    @line_h.setter
    def line_h(self, line_h):
        if line_h < 1:
            line_h = 1
        self.__line_h = line_h
        self.__save()

    @property
    def line_y(self):
        self.__read_from_property()
        return self.__line_y

    @line_y.setter
    def line_y(self, line_y):
        if line_y < 0:
            line_y = 0
        self.__line_y = line_y
        self.__save()

    @property
    def image_path(self):
        self.__read_from_property()
        return self.__image_path

    @image_path.setter
    def image_path(self, image_path):
        self.__image_path = image_path
        self.__save()

    def __str__(self):
        return self.get_as_dict().__str__()