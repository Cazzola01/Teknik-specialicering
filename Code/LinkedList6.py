class Node:
    def __init__(self, d, n=None):#Konstruktor
        self.data = d
        self.next = n
    def get_next(self):
        return self.next
    def set_next(self, n):
        self.next = n
    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data = d

class LinkedList: #Håller koll och kopplar ihop Nodes
    def __init__(self, r=None): #Konstruktor
        self.root = r
        self.size = 0
    def AddFirst(self, d): #Puttar in och den nya Node som första elementet i linkedlist
        new_node = Node(d, n=self.root) #Pekar på det första elementet att det blir next
        self.root = new_node #Puttar in och den nya Node, blir det första elementet(root)
        self.size += 1
    def AddLast(self, d): #(Add)
        new_node = Node(d, n=None)
        this_node = self.root #Börjar från root
        if this_node == None: #Om listan är tom, så sätter man new_node på sista plats
            self.root = new_node
        elif this_node:
            while this_node.get_next(): #Loop tills det inte finns en Node efter
                this_node = this_node.get_next()  # ny this_node
            this_node.set_next(new_node)  # det finns ingen efter, är i slutet, sätt dit node
        self.size += 1

    def AddAt(self, index, d):
        for x in range(index):
            pass



    def remove(self, d):
        this_node = self.root #Start looking at the root
        prev_node = None
        while this_node: #Looping trought all Nodes
            if this_node.get_data() == d: #hittade data
                if prev_node: #finns det någon Node framför, bara om lenght > 1
                    #kopplar om. Föregående node's next blir this_node next node
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next() #kopplar om, andra Node blir första
                self.size -= 1
                return True #Found item and deleted it

            else: #hittade inte data
                #uppdaterar noderna
                prev_node = this_node #sätter den gamla
                this_node = this_node.get_next() #ny this_node
        return False #Did not find item
    def find(self, d):
        this_node = self.root #Börjar kolla första element
        while this_node: #Är det något i root
            if this_node.get_data() == d:
                return True #Found it
            else:
                this_node = this_node.get_next()
        return False #did not find it
    def Length(self):
        return self.size

#Code
currentLinkedList = LinkedList()
currentLinkedList.AddLast(2)
currentLinkedList.AddLast(3)
currentLinkedList.AddLast(4)



