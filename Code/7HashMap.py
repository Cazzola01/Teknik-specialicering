from Code.LinkedList6 import LinkedList


class HashMap:
    def __init__(self, size):  # Konstruktor
        self.size = size
        self.LinkedListArray = self.AddLinkedLists()

    def AddLinkedLists(self):  # Runs when the Hashmap is created
        temp_list = []
        for i in range(self.size):
            temp_list.append(LinkedList())  # Array of LinkedLists
        return temp_list

    def GetIndex(self, key):  # Used to get index, When I have the key
        # key = hash(key)
        index = key % self.size  # Modelus on key
        return index

    def Put(self, key, value):  # Add a new element
        index = self.GetIndex(key)
        self.LinkedListArray[index].AddFirst([key, value])  # adding to linkedList

    def Find(self, key, value):  # true/false if it found the value
        index = self.GetIndex(key)
        print(self.LinkedListArray[index].Find([key, value]))  # Print true/false if found the value

    def Get(self, key):  # returns the value in the key
        index = self.GetIndex(key)
        print(self.LinkedListArray[index].Get(key))

    def ContainsKey(self, key):  # true/false om key finns
        index = self.GetIndex(key)
        print(self.LinkedListArray[index].ContainsKey(key))

    def ContainsValue(self, value):  # kollar om value finns någonstans i hashmap
        for x in range(self.size):  # Vanlig for loop
            if self.LinkedListArray[x].ContainsValue(value):  # LinkedList function()
                return True
        return False

    def clear(self):  # clears Hashmap
        self = HashMap(size=self.size)

    def isEmpty(self):  # Return true/false if Hashmap is empty
        for x in range(self.size):
            if self.LinkedListArray[x].isEmpty() is False:  # Kollar om varje linked list är tom
                return False
        return True

    def print(self):  # Prints every value in Hashmap. Prints linkedLists as arrays
        for x in range(self.size):  # Vanlig for loop
            print(self.LinkedListArray[x].toList())  # Gör linkedList till array och printar uiut

    def LoadDistribute(self, loadFactor=0.75):
        filledNum = 0
        for x in range(self.size):  # Checks how many LinkedLists are filled
            filledNum += 1 if self.LinkedListArray[x].isEmpty() is False else 0

        if filledNum / self.size > loadFactor:
            print('hey')
            oldSize = self.size
            newSize = self.size * 2  # Making the size the double
            newHashMap = HashMap(size=newSize)

            for x in range(oldSize):  # Looping trought every LinkedList
                for element in self.LinkedListArray[x].toList():  # Making every LinkedList an array
                    # element = [<key>, <value>]
                    key = element[0]
                    value = element[1]
                    newHashMap.Put(key, value)
            self = newHashMap  # Hashmap = newHashMap


hashmap = HashMap(size=2)
hashmap.Put(key=0, value=[43, 4343])  # Key= "user", value=value
hashmap.Put(key=1, value=[43, 4343])  # Key= "user", value=value
hashmap.print()

print("")

hashmap.LoadDistribute(0.75)
hashmap.print()
