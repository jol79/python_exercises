"""
 class with:
    1) getString -> to get a string from console inp
    2) printString -> prints string in upper case
    3) test function to test class methods
"""
class example(object):

    def __init__(self, input_data=str(raw_input())):
        self.__string_value = input_data

    def printString(self):
        print(self.__string_value.upper())

    
out = example()
out.printString()
