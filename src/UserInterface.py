from src.Deck import Deck
from src.Menu import Menu

class UserInterface():
    def __init__(self):
        self.__m_currentDeck = None


    def run(self):
        """Present the main menu to the user and repeatedly prompt for a valid command"""
        print("Welcome to the Bingo! Deck Generator\n")
        menu = Menu("Main")
        menu.addOption("C", "Create a new deck")
        
        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "C":
                self.__createDeck()
            elif command == "X":
                keepGoing = False


    def __createDeck(self):
        """Command to create a new Deck"""
        # TODO: Get the user to specify the card size, max number, and number of cards
        size = self.__getNumberInput("Card Size: ")
        while size < 3 or size > 15:
            print("That is not a valid size!\n")
            size = self.__getNumberInput("Card Size: ")

        max_num = self.__getNumberInput("\nMax Number: ")
        while max_num < 2*size*size or max_num > 4*size*size:
            print("That is not a valid max number!\n")
            max_num = self.__getNumberInput("Max Number: ")

        num_cards = self.__getNumberInput("\nNumber of Cards: ")
        while num_cards < 3 or num_cards > 10000:
            print("That is not a valid number of cards!\n")
            num_cards = self.__getNumberInput("Number of Cards: ", )
        # TODO: Create a new deck
        self.__m_currentDeck = Deck(size, num_cards, max_num)
        # TODO: Display a deck menu and allow use to do things with the deck
        self.__deckMenu()


    def __deckMenu(self):
        """Present the deck menu to user until a valid selection is chosen"""
        menu = Menu("Deck")
        menu.addOption("P", "Print a card to the screen")
        menu.addOption("D", "Display the whole deck to the screen")
        menu.addOption("S", "Save the whole deck to a file")

        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "P":
                self.__printCard()
            elif command == "D":
                print()
                self.__m_currentDeck.print()
            elif command == "S":
                self.__saveDeck()
            elif command == "X":
                keepGoing = False


    def __printCard(self):
        """Command to print a single card"""
        cardToPrint = self.__getNumberInput("Id of card to print: ")#, 1, self.__m_currentDeck.getCardCount())
        if cardToPrint > 0 and cardToPrint <= self.__m_currentDeck.getCardCount():
            print()
            self.__m_currentDeck.print(idx=cardToPrint)
        else:
            print("Can't print card! Invalid card ID!")


    def __saveDeck(self):
        """Command to save a deck to a file"""
        fileName = self.__getStringInput("Enter output file name: ")
        if fileName != "":
            # TODO: open a file and pass to currentDeck.print()
            outputStream = open(fileName, 'w')
            self.__m_currentDeck.print(outputStream)
            outputStream.close()
            print("Done!")

    def __getNumberInput(self, prompt):
        return int(input(prompt))

    def __getStringInput(self, prompt):
        return input(prompt)
