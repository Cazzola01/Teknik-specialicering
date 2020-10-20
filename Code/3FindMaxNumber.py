def max_num(l):
    curr_max = 0
    for number in l: #looping all number
        if number > curr_max: #if bigest so far
            curr_max = number #assign it as current max
    return curr_max

l = [2,5,3,4,6,2]
print(max_num(l))
print(max(l))

