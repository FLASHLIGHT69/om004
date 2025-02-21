def second_smallest(lst):
    unique_lst = list(set(lst))  
    unique_lst.sort()
    if len(unique_lst) > 1:
        return unique_lst[1]  
    else:
        return None  


lst = [7, 2, 5, 3, 8, 2]
second_small = second_smallest(lst)
print("Second Smallest Number:", second_small)
