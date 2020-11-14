from Code.HashMap7 import HashMap

longArr = [11, 1, 13, 21, 3, 7]
shortArr = [11, 3, 7, 13]

def CheckSubset(longArr, shortArr):
    found_it = False
    for short_i in shortArr:
        for long_i in longArr:
            if short_i == long_i:
                found_it = True #Make True check next element
                break #Next check
        if found_it is False: #Still false, means not found
            return False
        found_it = False #Changeing back
    return True

def CheckSubsetHashmap(longArr, shortArr):
    #Empty Hahsmaps
    longArr_hash = HashMap(size=6)
    shortArr_hash = HashMap(size=6)
    #Putting values in the Hashmaps
    for x in longArr:
        longArr_hash.Put(x,x)
    for x in shortArr:
        shortArr_hash.Put(x,x)

    #Checking
    for x in shortArr:
        if longArr_hash.ContainsKey(x):
            pass
        else:
            return False
    return True

print(CheckSubset(longArr=longArr, shortArr=shortArr))
print(CheckSubsetHashmap(longArr=longArr, shortArr=shortArr))