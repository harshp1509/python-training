def diff_bet_max_and_min(a):
    even_num = [num for num in a if num % 2 == 0]
    odd_num = [num for num in a if num % 2 != 0]

    max_even = max(even_num) 
    min_odd = min(odd_num)

    return max_even - min_odd

arr = [3, 5, 1, 8, 4, 9, 12, 7]
result = diff_bet_max_and_min(arr)

print(f"The difference between the maximum even and minimum odd numbers is: {result}")
