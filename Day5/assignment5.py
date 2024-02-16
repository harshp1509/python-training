# Write a program that takes a number as input from the user and displays whether the number is even or odd.

# a=int(input("enter the number..."))
# print("given number is even") if a%2==0 else print("given number is odd")

# Write a program that takes a list of numbers as input from the user and displays the sum of all the even numbers in the list.
# l1=input("Enter the list element...")
# l1=list(map(int,l1.split()))
# s=0
# for i in l1:
#     s+=i
# print(s)


# Write a program that displays the numbers from 1 to 10 using a for loop. 

# for i in range(10): print(i+1)

# Write a program that takes a number as input from the user and displays the multiplication table of the number using a while loop.
t=int(input("enter the number for mualtiplication table..."))
for i in range(10):
    print(f"{t} * {i+1} = {t*(i+1)}")

# Write a program that takes a list of numbers as input from the user and displays only the odd numbers in the list using a for loop.
l2=input("enter the list of numbers")
l2=list(map(int,l2.split()))

for i in l2:
    if(i%2!=0):
        print(i)

# Write a program that takes a number as input from the user and displays whether the number is prime or not using a try-except block.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    user_input = int(input("Enter a number: "))
    result = is_prime(user_input)

    if result:
        print(f"{user_input} is a prime number.")
    else:
        print(f"{user_input} is not a prime number.")
except ValueError:
    print("Please enter a valid integer.")
except Exception as e:
    print(f"An error occurred: {e}")


