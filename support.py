#All support methods will be in this file. I really do not need a class for this
#but personally, I think it helps me better organize my code.

class Support():

    #This method will allow the user to quit the program.
    def quit(self):
        print('\033c')
        print('Thank you for using this program! Please come again!')
        print()
        input('Press Enter to close out ')
