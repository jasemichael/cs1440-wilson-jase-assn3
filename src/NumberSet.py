import random

class NumberSet():
    def __init__(self, size):
        """NumberSet constructor"""
        self.__size = size
        self.__nums = []
        self.__increment = 0
        for i in range(1, size):
            self.__nums.append(i)

    def getSize(self):
        """Return an integer: the size of the NumberSet"""
        return self.__size

    def get(self, index):
        """Return an integer: get the number from this NumberSet at an index"""
        if index >= 0 and index < len(self.__nums)-1:
            return self.__nums[index]
        else:
            return None


    def randomize(self):
        """void function: Shuffle this NumberSet"""
        random.shuffle(self.__nums)


    def getNext(self):
        """Return an integer: when called repeatedly return successive values
        from the NumberSet until the end is reached, at which time 'None' is returned"""
        if self.get(self.__increment) == None:
            return None
        self.__increment += 1
        return self.get(self.__increment-1)
