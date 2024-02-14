def unique_ele(a):
    res = 0
    for num in a:
        res ^= num
    return res

arr = [1,2,2,3,1]
result = unique_ele(arr)

print(f"unique element in the array is: {result}")
