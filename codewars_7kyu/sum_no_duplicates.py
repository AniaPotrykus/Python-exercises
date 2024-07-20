# Please write a function that sums a list, but ignores any duplicated items in the list.

# For instance, for the list [3, 4, 3, 6] the function should return 10,
# and for the list [1, 10, 3, 10, 10] the function should return 4.

def sum_no_duplicates(l):
    
    dup_l = []
    new_l = []
    
    for el in l:
        if el not in new_l:
            new_l.append(el)
        else:
            dup_l.append(el)
            
    for el in dup_l: 
        if el in new_l:
            new_l.remove(el)
        
    return sum(new_l)