def find_con(a):
    min_el=min(a)
    max_el=max(a)
    b=(max_el*(max_el+1))/2 -(min_el*(min_el-1))/2 
    s=0

    for i in a:
        s+=i
    

    if s==b:
        return 1
    else:
        return 0
    
print(find_con([3,2,6,4,5]))
print(find_con([1,3,2,5]))


def dismulti(a):
    a=str(a)
    n=len(a)
    hs=set()
    for i in range(n):
        prod=1
        for j in range(i,n):
            prod=prod*int(a[j])
            if(prod in hs):
                return 0
            else:
                hs.add(prod)
    return 1

print(dismulti(23))
print(dismulti(236))
