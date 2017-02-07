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

    #This method will show the user the amount of right wing terrorist plots
    #and attacks that were committed by Jihadist terrorists.
    def jihadist(self):
        print('\033c')
        print('Here is the data for right wing terrorism: ')
        print()
        self.__total_deaths = len(self.__data)
        self.__jihadist = self.__data[self.__data.plot_ideology == 'Jihadist']
        self.__jihadist = len(self.__jihadist)
        print(self.__jihadist, 'out of', self.__total_deaths, 'were Right wing '\
        'terrorist plots or attacks'  )
        print()
        input('Press Enter to return to the main menu ')

    #This method will show the user the amount of right wing terrorist plots
    #and attacks that were committed by right wing terrorists.
    def right_wing(self):
        print('\033c')
        print('Here is the data for right wing terrorism: ')
        print()
        self.__total_deaths = len(self.__data)
        self.__right_wing = self.__data[self.__data.plot_ideology == 'Right Wing']
        self.__right_wing = len(self.__right_wing)
        print(self.__right_wing, 'out of', self.__total_deaths, 'were Right wing '\
        'terrorist plots or attacks'  )
        print()
        input('Press Enter to return to the main menu ')
