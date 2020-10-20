import math

def logFind(l, numToFind):
    looptimes = math.floor(math.log2(len(l)))

    for x in range(looptimes): #Looping and trying to find num
        midPos = math.floor(len(l)/2) #The midpos of the list is the length/2 and then floored
        midNum = l[midPos] #Assigning the middle number to midNum variable
        if numToFind == midNum: #Found the number
            return True
        elif numToFind > midNum: #Number is bigger then midNum
            l = l[midPos+1:] #removing all rumbers before midPos. +1 because we dont want the midNum
        elif numToFind < midNum: #Number is smaller then midNum
            l = l[:midPos] #removing all rumbers after midPos and the number at midPos
    return False

l = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
numToFind = 2
print(logFind(l, numToFind))