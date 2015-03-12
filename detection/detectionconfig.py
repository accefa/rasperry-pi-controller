# coding=utf-8
# Diese Klasse repräsentiert die Konfiguration welche in der Datei config.json im Hauptverzeichnisses des Projektes
# gespeichert ist. Normalerweise werden die Werte über die Methoden set/get_from_dict oder direkt über die Properties
# bearbeitet. Es ist auch möglich die Datei config.json zu bearbeiten.

import os
import json


class DetectionConfig(object):
    CONFIG_FILE_PATH = os.path.dirname(__file__) + '/../config.json'

    __QUALITY_DEFAULT = 90
    _QUALITY_KEY = 'quality'
    __CROP_X_DEFAULT = 0
    _CROP_X_KEY = 'crop_x'
    __CONTRAST_DEFAULT = 0
    _CONTRAST_KEY = 'contrast'
    __GREYSCALE_DEFAULT = True
    _GREYSCALE_KEY = 'greyscale'
    __GREYSCALE_THRESHOLD_DEFAULT = 0
    _GREYSCALE_THRESHOLD_KEY = 'greyscale_threshold'
    __LINE_H_DEFAULT = 1
    _LINE_H_KEY = 'line_h'
    __LINE_Y_DEFAULT = 0
    _LINE_Y_KEY = 'line_y'
    __IMAGE_PATH_DEFAULT = os.path.dirname(__file__) + '/../images'
    _IMAGE_PATH_KEY = 'image_path'

    __default_dict = {
        _QUALITY_KEY: __QUALITY_DEFAULT,
        _CROP_X_KEY: __CROP_X_DEFAULT,
        _CONTRAST_KEY: __CONTRAST_DEFAULT,
        _GREYSCALE_KEY: __GREYSCALE_DEFAULT,
        _GREYSCALE_THRESHOLD_KEY: __GREYSCALE_THRESHOLD_DEFAULT,
        _LINE_H_KEY: __LINE_H_DEFAULT,
        _LINE_Y_KEY: __LINE_Y_DEFAULT,
        _IMAGE_PATH_KEY: __IMAGE_PATH_DEFAULT
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
            self._QUALITY_KEY: self.quality,
            self._CROP_X_KEY: self.crop_x,
            self._CONTRAST_KEY: self.contrast,
            self._GREYSCALE_KEY: self.greyscale,
            self._GREYSCALE_THRESHOLD_KEY: self.greyscale_threshold,
            self._LINE_H_KEY: self.line_h,
            self._LINE_Y_KEY: self.line_y,
            self._IMAGE_PATH_KEY: self.image_path
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

        if self._QUALITY_KEY in config_dict:
            self.quality = config_dict[self._QUALITY_KEY]

        if self._CROP_X_KEY in config_dict:
            self.crop_x = config_dict[self._CROP_X_KEY]

        if self._CONTRAST_KEY in config_dict:
            self.contrast = config_dict[self._CONTRAST_KEY]

        if self._GREYSCALE_KEY in config_dict:
            self.greyscale = config_dict[self._GREYSCALE_KEY]

        if self._GREYSCALE_THRESHOLD_KEY in config_dict:
            self.greyscale_threshold = config_dict[self._GREYSCALE_THRESHOLD_KEY]

        if self._LINE_H_KEY in config_dict:
            self.line_h = config_dict[self._LINE_H_KEY]

        if self._LINE_Y_KEY in config_dict:
            self.line_y = config_dict[self._LINE_Y_KEY]

        if self._IMAGE_PATH_KEY in config_dict:
            self.image_path = config_dict[self._IMAGE_PATH_KEY]

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