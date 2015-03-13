# coding=utf-8

import os
import json
import logging

LEVEL_DEFAULT = logging.INFO
LEVEL_KEY = 'level'

class LoggerConfig(object):
    CONFIG_FILE_PATH = os.path.dirname(__file__) + '/logger_config.json'
    FILE_PATH = os.path.dirname(__file__) + '/../main.log'
    FORMAT = '%(asctime)s %(levelname)s %(message)s'
    DATE_FORMAT = '%d/%m/%Y %H:%M:%S'

    __default_dict = {
        LEVEL_KEY: LEVEL_DEFAULT
    }

    __test = [
        logging.CRITICAL,
        logging.ERROR,
        logging.WARNING,
        logging.INFO,
        logging.DEBUG
    ]

    __populate_in_progress = False
    __save_in_progress = False

    def __init__(self):
        self.__read()

    def set_from_dict(self, config_dict):
        self.__populate(config_dict)
        self.__save()

    def get_as_dict(self):
        return {
            LEVEL_KEY: self.level
        }

    def __read(self):
        try:
            config_dict = self.__read_config_from_file()
            self.__populate(config_dict)
        except (TypeError, ValueError, IOError) as e:
            config_dict = self.__default_dict
            self.__populate(config_dict)
            self.__save()

    def __read_config_from_file(self):
        with open(self.CONFIG_FILE_PATH) as config_file:
            return json.load(config_file)

    def __populate(self, config_dict):
        self.__populate_in_progress = True

        if LEVEL_KEY in config_dict:
            self.level = config_dict[LEVEL_KEY]

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
    def level(self):
        self.__read_from_property()
        return self.__level

    @level.setter
    def level(self, level):
        if level in self.__test:
            self.__level = level
            self.__save()

    def __str__(self):
        return self.get_as_dict().__str__()