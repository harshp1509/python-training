arr=[2,4,1,3,2]

max_ele=max(arr)

ans=0

for i in arr:
    if i!=max_ele:
        ans+=max_ele-i
    
print(ans)