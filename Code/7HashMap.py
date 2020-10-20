from LinkedList6 import LinkedList

class HashMap:
    def __init__(self, size):#Konstruktor
        self.size = size
        self.LinkedListArray = self.AddLinkedLists()

    def AddLinkedLists(self):
        temp_list = []
        for i in range(self.size):
            temp_list.append(LinkedList)
        return temp_list



    def HashFunction(self, value): #Make value an int
        #if value.dtype() = int
        #if value.dtype() = float
        #if value.dtype() = string/char

        key = value #Eftersom value är en int, så kan nykeln vara samma
        return key

    def GetIndex(self, key):
        index = key % self.size
        return index

    def put(self, value):
        key = self.HashFunction(self, value)
        index = self.GetIndex(key)
        self.LinkedListArray[index].AddFirst(value)

HashMap(size=6)
HashMap.put(43)


