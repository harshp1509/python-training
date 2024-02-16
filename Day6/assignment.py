import my_module

# Write a program that defines a function to calculate the area of a rectangle. The function should take the length and width of the rectangle as input parameters and return the area.

def area(width,height):
    return width*height

print(area(10,52))

# Write a program that defines a function to calculate the factorial of a number. The function should take a single input parameter and return the factorial of that number.

def fact(a):
    if(a==1 or a==2):
        return a
    else:
        return a*fact(a-1)
    
print(fact(10))

# Write a program that defines a function to calculate the sum of a list of numbers. The function should take a list of numbers as input and return the sum of those numbers.

def sum_list(l):
    return(sum(l))

print(sum_list([1,5,3,6,7,6,65]))

# Write a program that defines a function to calculate the nth Fibonacci number. The function should take a single input parameter and return the nth Fibonacci number.

def fibo(n):
    if(n==1):
        return 0
    elif(n==1 or n==2):
        return 1
    else:
        return fibo(n-2)+fibo(n-1)
    
print(fibo(10))

# Create a module called my_module that defines a function to calculate the square of a number. Import the module into a new program and use the function to calculate the square of a number.

def squre_no(n):
    return my_module.squre(n)

print(squre_no(10))