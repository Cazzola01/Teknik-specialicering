def prefix_sum_quadratic(l):
    res = []
    for index in range(len(l)):
        curr_sum = 0
        for i in range(index+1):
            curr_sum += l[i]
        res.append(curr_sum)
    return res

l = [1,4,3,2,6,5] #res -> [1,5,8,10,16,21]
res = prefix_sum_quadratic(l)
print("prefix sum:")
print(l)
print(res)