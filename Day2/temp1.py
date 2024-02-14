age=25
name="Harsh"
temperature=29.5
l=5
w=10
area=l*w
age=age+1


def decimaltobinary(n):
    if n>=1:
        decimaltobinary(n//2)
    print(n%2, end= '')

decimaltobinary(5)
print()
decimaltobinary(7)
