class Calculator(object):
    def __init__(self):
        self.__history = []

    def add_to_history(self, sentence):
        self.__history.append(sentence)

    def add(self, num1, num2):
        result = num1 + num2
        self.add_to_history('{} + {} = {}'.format(num1, num2, result))
        return result

    def substract(self, num1, num2):
        result = num1 - num2
        self.add_to_history('{} - {} = {}'.format(num1, num2, result))
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.add_to_history('{} * {} = {}'.format(num1, num2, result))
        return result

    def divide(self, num1, num2):
        if num2 != 0:
            result = num1 / num2
            self.add_to_history('{} / {} = {}'.format(num1, num2, result))
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

class AdvancedCalculator(Calculator):
    def root(self, num1, num2):
        result = num1 ** (1/num2)
        self.add_to_history('Pierwiastek {} stopnia z {} wynosi {}'.format(num2, num1, result))
        return result

    def pow(self, num1, num2):
        result = num1 ** num2
        self.add_to_history('{} ** {} = {}'.format(num1, num2, result))
        return result

new = AdvancedCalculator()
new.root(8,3)
new.pow(2,3)
new.printOperations()
new.clearOperations()
new.printOperations()