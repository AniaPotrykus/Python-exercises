#In this kata the aim is to compare each pair of integers from two arrays, and return a new array of large numbers.

#Note: Both arrays have the same dimensions.

#Example:
#arr1 = [13, 64, 15, 17, 88]
#arr2 = [23, 14, 53, 17, 80]
#get_larger_numbers(arr1, arr2) == [23, 64, 53, 17, 88]

def get_larger_numbers(a, b):
    
    large = []
    
    i = 0
    
    for el in a:
        if el >= b[i]:
            large.append(el)
            i += 1
            
        else: 
            large.append(b[i])
            i += 1
            
    return large

    # solution with zip()

    def get_larger_numbers(a, b):

        zipped = zip(a, b)

        l = []

        for x, y in zipped:
            if x > y:
                l.append(x)
            else:
                l.append(y)

        return l