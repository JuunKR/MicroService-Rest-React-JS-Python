from django.db import models
# Create your models here.
from juun.common.models import FileDTO
from juun.common.models import Reader, Printer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import time
import re


class Services():

    file = FileDTO()
    reader = Reader()
    printer = Printer()
    driver_path = 'C:\\Program Files\\Google\\Chrome\\chromedriver'
    menu_ls = []
    name_ls = []
    rank_ls = []
    url_ls = []
    saved_url = []

    def set_url(self):
        f = self.file
        f.url = 'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago'
        # f.url = requests.get(f.url, headers={'User-Agent': 'Mozilla/5.0'}).text



    def get_sandwich(self):
        f = self.file
        print(f.url)
        driver = webdriver.Chrome(self.driver_path)
        driver.get(f.url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        list = soup.find_all('div', {'class':'sammy'})
        # print(list)
        for i in list:
            self.rank_ls.append(i.find(class_='sammyRank').text)
            tmp_string = i.find(class_='sammyListing').text

            self.name_ls.append(re.split(('\n|\r\n'), tmp_string)[1])
            self.menu_ls.append(re.split(('\n|\r\n'), tmp_string)[0])


        for i in self.name_ls:
            tmp = i
            tmp = tmp.replace(' ', '-')
            for j in self.menu_ls:
                tmp2 = j
                tmp2 = tmp2.replace(' ', '-')
                self.url_ls.append('-in-'+ tmp + '-' + tmp2)

        for i in self.url_ls:
            self.saved_url.append(self.file.url + i)
        print(self.saved_url)

        # [self.menu_ls.append(i.find('b').text) for i in test1]
        # [self.name_ls.append(i.find('a')) for i in test1]
        # print(self.menu_ls)
        # print(self.name_ls)


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
    # test = 'Old Oak Tap'
    # test3 = 'BLT'
    # test2 = test.replace(' ', '-')
    # test5 = '-' + test2 + '-' + test3
    # print(test5)