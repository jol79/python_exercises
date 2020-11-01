class example(object):
    def __init__(self):
        self.__string_value = ""

    def setString(self):
        self.string_value = self.__string_value

    def getString(self):
        self.string_value = input()

    def printString(self):
        return self.string_value.upper()

    
out = example()
out.getString()
out.printString()