from Code.LinkedList6 import LinkedList

class HashMap:
    def __init__(self, size):#Konstruktor
        self.size = size
        self.LinkedListArray = self.AddLinkedLists()

    def AddLinkedLists(self):
        temp_list = []
        for i in range(self.size):
            temp_list.append(LinkedList())
        return temp_list

    def SetToInt(self, value): #Make value an int
        #if value.dtype() = int
        #if value.dtype() = float
        #if value.dtype() = string/char

        #key = hash(value) #Eftersom value är en int, så kan nykeln vara samma
        key = value
        return key

    def GetIndex(self, key):
        index = key % self.size
        return index

    def put(self, value):
        key = self.SetToInt(value)
        index = self.GetIndex(key)
        self.LinkedListArray[index].AddFirst(value)

hashmap = HashMap(size=6)
hashmap.put(43)


