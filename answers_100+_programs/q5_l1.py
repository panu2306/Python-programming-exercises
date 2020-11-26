'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class StringClass:
    def __init__(self):
        self.input_string = ''
    
    def getString(self):
        self.input_string = input('Enter a string: ')    

    def printString(self):
        print(self.input_string.upper())

s = StringClass()
s.getString()
s.printString()
