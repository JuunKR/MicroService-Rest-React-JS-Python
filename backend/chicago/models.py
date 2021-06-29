# Create your models here.
from common.models import FileDTO
from bs4 import BeautifulSoup
import requests
import re
from icecream import ic
from tqdm import tqdm



class Services(object):

    file = FileDTO()
    driver_path = 'C:\\Program Files\\Google\\Chrome\\chromedriver'
    menu_ls = []
    name_ls = []
    rank_ls = []
    url_ls = []
    new_url = []
    price = []
    address = []
    tel = []
    home_page = []


    def set_url(self):
        f = self.file
        f.url = 'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago'
        f.url = requests.get(f.url, headers={'User-Agent': 'Mozilla/5.0'}).text




    def get_sandwich(self):
        f = self.file

        # driver = webdriver.Chrome(self.driver_path)
        # driver.get(f.url)
        # soup = BeautifulSoup(driver.page_source, 'lxml')
        soup = BeautifulSoup(f.url, 'lxml')

        list = soup.find_all('div', {'class':'sammy'})

        # print(list)

        for i in list:
            self.rank_ls.append(i.find(class_='sammyRank').text)
            self.url_ls.append(i.find('a')['href'])
            tmp_string = i.find(class_='sammyListing').text


            self.name_ls.append(re.split(('\n|\r\n'), tmp_string)[1])
            self.menu_ls.append(re.split(('\n|\r\n'), tmp_string)[0])

        for i in self.url_ls:
            tmp = i.split('/November-2012/')[1]
            tmp = 'https://www.chicagomag.com/Chicago-Magazine/November-2012/' + tmp
            self.new_url.append(tmp)


    def get_sandwiches(self):
        tmp = []
        for i in tqdm(self.new_url):
            url = requests.get(i, headers={'User-Agent': 'Mozilla/5.0'}).text
            soup = BeautifulSoup(url, 'lxml')
            list = soup.find_all('p', {'class': 'addy'})

            # driver = webdriver.Chrome(self.driver_path)
            # driver.get(i)
            # soup = BeautifulSoup(driver.page_source, 'lxml')
            for j in list:
                # tmp.append((j.find('em').text))

                self.price.append((j.find('em').text).split()[0][:-1])
                # a = j.select_one('em').a.decompose().text
                # ic(a)
                # print(a)
                self.address.append(''.join(j.find('em').text.split()[1:-2]))
                self.tel.append(re.search('\d{2,3}-\d{3,4}-\d{4}',(j.find('em').text)))

                # self.home_page.append((j.find('em').text).split()[-1:])
        ic(tmp)
        ic(self.price)
        ic(self.address)
        print(type(self.tel[1]))
        # ic(self.home_page)















if __name__ == '__main__':
    s=Services()
    s.set_url()
    s.get_sandwich()
    # test = 'Old Oak Tap'
    # test3 = 'BLT'
    # test2 = test.replace(' ', '-')
    # test5 = '-' + test2 + '-' + test3
    # print(test5)
    s.get_sandwiches()