#This is the main file of the program that will hold all of the functions
#which will be used to run the program.

#Files which will be imported.
from valid import *
from data import *


def main():
    print('\033c')
    print('\t---------------------------------')
    print('\tWelcome to US Terrorism Information')
    print('\t---------------------------------')
    print()
    input('Press enter to head to main menu ')
    main_menu()

def main_menu():
    print('\033c')
    print('1. Look at plots by ideology')
    choice = int(input('What is your choice: '))
    data = Data()
    if choice == 1:
        idealogy(data)

def idealogy(data):
    print('\033c')

main()
