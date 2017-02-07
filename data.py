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
