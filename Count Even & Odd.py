def count_even_odd(lst):
    even_count = 0
    odd_count = 0
    
    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return even_count, odd_count

# Taking input from the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

even, odd = count_even_odd(numbers)

print(f"Number of even elements: {even}")
print(f"Number of odd elements: {odd}")
