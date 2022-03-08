# coding: utf-8
import argparse
from abc import ABCMeta, abstractmethod
from importlib.metadata import entry_points, version

class BaseView(metaclass=ABCMeta):

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.__define_common_options()

    def __define_common_options(self):
        self.parser.add_argument("--version", "-v", action="version", version=version(entry_points().get('name')))
        self.parser.add_argument("--quiet", "-q", action='store_true', help="flag to suppress standard output.")

    @abstractmethod
    def define_options(self):
        pass
