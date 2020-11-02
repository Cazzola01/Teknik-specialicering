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
        key = hash(value)
        return key

    def GetIndex(self, key):
        index = key % self.size
        return index

    def Put(self, key, value):
        index = self.GetIndex(key)
        self.LinkedListArray[index].AddFirst([key, value])

    def Find(self, key, value):
        index = self.GetIndex(key)
        print(self.LinkedListArray[index].Find([key, value])) #Print true/false if it found the value

    def Get(self, key):
        index = self.GetIndex(key)
        print(self.LinkedListArray[index].Get(key))

    def ContainsKey(self, key):
        index = self.GetIndex(key)
        print(self.LinkedListArray[index].ContainsKey(key))
    def ContainsValue(self, value):
        for x in range(self.size):
            if self.LinkedListArray[x].ContainsValue(value):
                print(True)
                return True
        print(False)
        return False


hashmap = HashMap(size=6)
hashmap.Put(key=3, value=[43,4343]) #Key= "user", value=value
#hashmap.Find(key=3, value=43)
hashmap.Get(key=3)
hashmap.ContainsKey(key=6)
hashmap.ContainsValue(value=[43,4343])



