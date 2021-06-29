from django.db import models

# Create your models here.
from abc import *
from dataclasses import dataclass
import json
import googlemaps
import pandas as pd
from selenium import webdriver

@dataclass
class FileDTO(object):

    context: str
    fname: str
    url : str
    dframe: object

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def url(self) -> str: return self._url

    @url.setter
    def url(self, url): self._url = url

    @property
    def dframe(self) -> object: return self._dframe

    @dframe.setter
    def dframe(self, dframe): self._dframe = dframe

class PrinterBase(metaclass=ABCMeta):
    @abstractmethod
    def dframe(self):
        pass

class ReaderBase(metaclass=ABCMeta):

    @abstractmethod
    def new_file(self):
        pass

    @abstractmethod
    def csv(self):
        pass

    @abstractmethod
    def xls(self):
        pass

    @abstractmethod
    def json(self):
        pass

class ScraperBase(metaclass=ABCMeta):

    @abstractmethod
    def driver(self):
        pass


class Printer(PrinterBase):

    def dframe(self, this):
        print('*' * 100)
        print(f'1. Target type \n {type(this)} ')
        print(f'2. Target column \n {this.columns} ')
        print(f'3. Target 상위 1개 행\n {this.head()} ')
        print(f'4. Target null    의 갯수\n {this.isnull().sum()}개')
        print('*' * 100)


class Reader(ReaderBase):

    def new_file(self, file) -> str:
        return file.context + file.fname

    def csv(self, file) -> object:
        return pd.read_csv(f'{self.new_file(file)}.csv', encoding='UTF-8', thousands=',')

    def xls(self, file, header, usecols) -> object:
        return pd.read_excel(f'{self.new_file(file)}.xls', header=header, usecols=usecols)

    def csv_header(self, file, header) -> object:
        return pd.read_csv(f'{self.new_file(file)}.csv', encoding='UTF-8', thousands=',', header=header)


    def json(self, file) -> object:
        return json.load(open(f'{self.new_file(file)}.json', encoding='UTF-8'))

    def gmaps(self) -> object:
        return googlemaps.Client()

class Scraper(ScraperBase):

    def driver(self) -> object:
        return webdriver.Chrome('C:/Program Files/Google/Chrome/chromedriver')

    def auto_login(self):
        pass
