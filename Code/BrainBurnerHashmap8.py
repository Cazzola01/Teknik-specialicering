from Code.HashMap7 import HashMap

arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 13]

def CheckSubset(arr1, arr2):
    found_it = False
    for check in arr2:
        for element in arr1:
            if element == check:
                found_it = True
                break #Next check
        if found_it is False:
            return False #Did not find
        found_it = False
    return True

def CheckSubsetHashmap(arr1, arr2):
    arr1_hash = HashMap(size=6)
    arr2_hash = HashMap(size=6)
    for x in arr1:
        arr1_hash.Put(x,x)
    for x in arr2:
        arr2_hash.Put(x,x)

    for x in arr2:
        if arr1_hash.ContainsKey(x) is False:
            return False
    return True
''':key
    for check in arr2:
        if arr1_hash.ContainsKey(check):
                found_it = True
        if found_it is False:
            return False #Did not find
        found_it = False
    return True
'''







print(CheckSubset(arr1=arr1, arr2=arr2))
print(CheckSubsetHashmap(arr1=arr1, arr2=arr2))