import sys
import NumberSet

class Card():
    def __init__(self, idnum, size, numberSet):
        """Card constructor"""
        self.__id = idnum
        self.__size = size
        self.__numberSet = numberSet
        self.__numberSet.randomize()
        self.generateCard()


    def getId(self):
        """Return an integer: the ID number of the card"""
        return self.__id

    def getSize(self):
        """Return an integer: the size of one dimension of the card.
        A 3x3 card will return 3, a 5x5 card will return 5, etc.
        """
        return self.__size

    def print(self, file=sys.stdout):
        """void function:
        Prints a card to the screen or to an open file object"""
        file.write(str(self))

    def generateCard(self):
        if self.__size % 2 == 0:
            self.__card = ""
            for i in range(self.__size):
                self.__card += ("+-----"*self.__size + "+" + "\n")
                for j in range(self.__size):
                    self.__card += ("|" + str(self.__numberSet.getNext()).center(5))
                self.__card += "|\n"
            self.__card += ("+-----" * self.__size + "+" + "\n")
        else:
            self.__card = ""
            for i in range(self.__size):
                self.__card += ("+-----" * self.__size + "+" + "\n")
                for j in range(self.__size):
                    if int(self.__size/2) == i and int(self.__size/2) == j:
                        self.__card += ("|" + "FREE!")
                        continue
                    self.__card += ("|" + str(self.__numberSet.getNext()).center(5))
                self.__card += "|\n"
            self.__card += ("+-----" * self.__size + "+" + "\n")
        return self.__card

    def __str__(self):
        """String representation of card"""
        return self.__card