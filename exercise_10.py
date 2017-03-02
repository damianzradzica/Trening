from random import randint



listOfNumbers = []
class BankAccount(object):
    def __init__(self):
        self.__cash = 0
        value = 100
        for i in listOfNumbers:
            if i == value:
                value += 1
            else:
                pass
        self.__number = value
        listOfNumbers.append(self.__number)

    def getNumber(self):
        return self.__number

    def getCash(self):
        return self.__cash

    def depositCash(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.__cash += amount
            return amount
        else:
            raise TypeError('wymagana jest wartość numeryczna większa od zera')

    def withdrawCash(self, amount):
        if isinstance(amount, int) and amount > 0:
            if self.__cash >= amount:
                self.__cash -= amount
                return amount
            else:
                withdraw = self.__cash
                self.__cash = 0
                return withdraw
        else:
            raise TypeError('wymagana jest wartość numeryczna większa od zera')

    def printInfo(self):
        print('Numer konta: {}, stan konta: {}'.format(self.__number, self.__cash))

marian = BankAccount()
print(marian.getNumber())
print(marian.getCash())
marian.depositCash(500)
marian.printInfo()
print(marian.withdrawCash(700))
marian.printInfo()

andrzej = BankAccount()
andrzej.printInfo()

