#This file will hold my data class.

#importing all libraries which will be used.
import pandas as pd
import numpy as np

#importing validation file
from valid import *

class Data():

    #This is the init method
    def __init__(self):
        self.__data = pd.read_csv('plots.csv')

    #This method will allow me to see all of the information that is contained
    #in the csv file.
    def show(self):
        return self.__data

    #This method will show the user the amount of right wing or Jihadist
    #terrorist plots and attacks.
    def idealogy_stats(self, data_type):
        print('\033c')
        print('Here is the data for', data_type, 'terrorism: ')
        print()
        self.__total_deaths = len(self.__data)
        self.__jihadist = self.__data[self.__data.plot_ideology == data_type]
        self.__jihadist = len(self.__jihadist)
        print(self.__jihadist, 'out of', self.__total_deaths, 'were', data_type, \
        'terrorist plots or attacks'  )
        print()
        input('Press Enter to return to the main menu ')

    #This method will allow the user to see attacks were a certain number of
    #people were killed.
    def deaths(self, number_deaths):
        print('\033c')
        self.__data = self.__data[self.__data.victims_killed >= number_deaths]
        print(self.__data)
        input('Hit enter to return to main menu ')

    #This method will allow the user to see the number of attacks that were
    #prevented versus not prevented
    def prevented(self):
        print('\033c')
        total_attacks = len(self.__data)
        print('\tHere is the data for prevented / not prevented:')
        print()
        print('\tThe total number of attacks is:',total_attacks)
        prevented = len(self.__data[self.__data.plot_status == 'Prevented'])
        not_prevented = len(self.__data[self.__data.plot_status == 'Not Prevented'])
        print('\tThe total number of prevented attacks is:', prevented)
        print('\tThe total number of prevented attacks is:', not_prevented)
        print('''
            Please note that there are not responses for all of the attacks. For
        this reason the number of prevented and not prevented attacks will not
        add up to the correct total.
        ''')
        input('Hit enter to return to main menu ')
