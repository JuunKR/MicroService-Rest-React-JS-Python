from django.shortcuts import render

# Create your views here.
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
from models import Service


class Crime_API(object):

    @staticmethod
    def main():
        service = Service()
        while 1:
            menu = input('0. exit\n'
                         '1. pop_in_seoul\n'
                         '2. cctv_in_seoul\n'
                         '3. crime_in_seoul\n'
                         '4. police_position\n'
                         )
            if menu == '0':
                break
            elif menu == '1':
                service.xls({'context':'./data/', 'fname':'pop_in_seoul'})
            elif menu == '2':
                service.csv({'context':'./data/', 'fname':'cctv_in_seoul'})
            elif menu == '3':
                service.csv({'context':'./data/', 'fname':'crime_in_seoul'})
            elif menu == '4':
                service.csv({'context':'./data/', 'fname':'police_position'})


            else:
                continue

Crime_API.main()