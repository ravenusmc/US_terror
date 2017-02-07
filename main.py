#This is the main file of the program that will hold all of the functions
#which will be used to run the program.

#Files which will be imported.
from valid import *
from data import *
from support import *

#This is the main function in the program which will be used to start it.
def main():
    print('\033c')
    print('\t---------------------------------')
    print('\tWelcome to US Terrorism Information')
    print('\t---------------------------------')
    print()
    input('Press enter to head to main menu ')
    main_menu()

#This function is the main menu of the program where the user may choose
#What they want to look at.
def main_menu():
    print('\033c')
    print('1. Look at plots by ideology')
    print('2. Quit')
    choice = int(input('What is your choice: '))
    data = Data()
    support = Support()
    if choice == 1:
        idealogy(data)
    elif choice == 2:
        support.quit()

#This is where the user may select the idealogy to look at for terrorist attacks
#The data that I have only has information on jihadist or right wing terrorist
#attacks or plots.
def idealogy(data):
    print('\033c')
    print('1. Jihadist')
    print('2. Right Wing')
    choice = int(input('What ideology do you want to see data for? '))
    while not two_valid(choice):
        print('That was not a proper selection!')
        choice = int(input('What ideology do you want to see data for? '))
    if choice == 1:
        data.jihadist()
        main_menu()
    elif choice == 2:
        data.right_wing()
        main_menu()

main()
