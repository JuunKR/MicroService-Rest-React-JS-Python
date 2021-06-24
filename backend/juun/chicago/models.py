from django.db import models
# Create your models here.
from juun.common.models import FileDTO
from juun.common.models import Reader, Printer
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests


class Services():

    def __init__(self):
        self.f = FileDTO()
        self.r = Reader()
        self.p = Printer()


    def set_url(self):
        f = self.f
        f.url = 'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'
        f.url = requests.get(f.url, headers={'User-Agent': 'Mozilla/5.0'}).text

    def get_sandwich(self):
        f = self.f
        soup = BeautifulSoup(f.url, 'lxml')
        print(soup)
        # tmp_one = soup.find_all('div', 'sammy')
        # print(tmp_one)

        # html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
        # html = urlopen(html).read()
        # soup = BeautifulSoup(html, "html.parser")
        # print(soup)


if __name__ == '__main__':
    s=Services()
    s.set_url()
    s.get_sandwich()