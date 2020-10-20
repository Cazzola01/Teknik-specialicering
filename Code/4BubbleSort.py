import random
import timeit
import functools

def bubble(l):
    for x in range(len(l)):
        for i in range(len(l) - 1): #-1 eftersom annars blir det index out of range, eftrsom amn skriver [i + 1]
            if l[i] > l[i + 1]: # om föregående tal är större
                l[i], l[i + 1] = l[i + 1], l[i] #swap
    return l

def bubble_effektiv(l):
    for x in range(len(l)):
        for i in range(len(l) - 1 - x): #-1 eftersom annars blir det index out of range, eftrsom amn skriver [i + 1]
            if l[i] > l[i + 1]: # om föregående tal är större
                l[i], l[i + 1] = l[i + 1], l[i] #swap
    return l

def randIntList(numElement):
    l = []
    for i in range(numElement):
        l.append(random.randint(0,1024))
    return l

l = randIntList(100) #Gör en lista med 100 random tal
print(timeit.timeit(functools.partial(bubble_effektiv, l), number=100000)) #Kör bubble_effektiv() 200 gånger
#l = bubble_effektiv(l)
#print("final ", l)
