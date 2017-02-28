class Calculator(object):
    def __init__(self):
        self.__history = []

    def __add_to_history(self, sentence):
        self.__history.append(sentence)

    def add(self, num1, num2):
        result = num1 + num2
        self.__add_to_history('{} + {} = {}'.format(num1, num2, result))
        return result

    def substract(self, num1, num2):
        result = num1 - num2
        self.__add_to_history('{} - {} = {}'.format(num1, num2, result))
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.__add_to_history('{} * {} = {}'.format(num1, num2, result))
        return result

    def divide(self, num1, num2):
        if num2 != 0:
            result = num1 / num2
            self.__add_to_history('{} / {} = {}'.format(num1, num2, result))
            return result
        else:
            raise ValueError('num2 nie może wynosić 0')

    def printOperations(self):
        print(self.__history)

    def clearOperations(self):
        self.__history = []

calc = Calculator()
calc.add(5,3)
calc.substract(4,6)
calc.multiply(2,2)
# calc.divide(4,0)
calc.divide(4,2)
calc.printOperations()
calc.clearOperations()
calc.printOperations()