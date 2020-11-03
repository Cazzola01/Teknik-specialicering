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

    def GetIndex(self, key):
        index = key % self.size
        return index

    def Put(self, key, value):
        index = self.GetIndex(key)
        self.LinkedListArray[index].AddFirst([key, value])

    def Find(self, key, value): #true/false if it found the value
        index = self.GetIndex(key)
        print(self.LinkedListArray[index].Find([key, value])) #Print true/false if it found the value

    def Get(self, key): # returns the value in the key
        index = self.GetIndex(key)
        print(self.LinkedListArray[index].Get(key))

    def ContainsKey(self, key): #true/false om key finns
        index = self.GetIndex(key)
        print(self.LinkedListArray[index].ContainsKey(key))
    def ContainsValue(self, value): #kollar om value finns någonstans i hashmap
        for x in range(self.size): #Vanlig for loop
            if self.LinkedListArray[x].ContainsValue(value):
                return True
        return False

    def clear(self):
        self = HashMap(size=self.size)

    def isEmpty(self):
        for x in range(self.size): #Vanlig for loop
            if self.LinkedListArray[x].isEmpty() is False:
                return False
        return True
    def print(self):
        for x in range(self.size): #Vanlig for loop
            print(self.LinkedListArray[x].toList())


hashmap = HashMap(size=6)
hashmap.Put(key=0, value=[43,4343]) #Key= "user", value=value
hashmap.Put(key=3, value=[43,4343]) #Key= "user", value=value
#hashmap.Find(key=3, value=43)
#hashmap.Get(key=3)
#hashmap.ContainsKey(key=6)
#hashmap.ContainsValue(value=[43,4343])
print(hashmap.isEmpty())
hashmap.print()


