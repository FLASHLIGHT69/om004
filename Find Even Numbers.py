def find_even_odd(lst):
    even_numbers = [x for x in lst if x % 2 == 0]
    odd_numbers = [x for x in lst if x % 2 != 0]
    return even_numbers, odd_numbers

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even, odd = find_even_odd(lst)
print("Even Numbers:", even)
print("Odd Numbers:", odd)
