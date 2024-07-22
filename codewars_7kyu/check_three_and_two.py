#Given an array with exactly 5 strings "a", "b" or "c" (chars in Java, characters in Fortran), check if the array contains three and two of the same values.

#Examples
#["a", "a", "a", "b", "b"] ==> true  // 3x "a" and 2x "b"
#["a", "b", "c", "b", "c"] ==> false // 1x "a", 2x "b" and 2x "c"
#["a", "a", "a", "a", "a"] ==> false // 5x "a"

def check_three_and_two(array):

    list_a = []
    list_b = []
    list_c = []

    for el in array:
        if el == "a":
            list_a.append(el)
        elif el == "b":
            list_b.append(el)
        elif el == "c":
            list_c.append(el)
            
    if (len(list_a) == 3 and len(list_b) == 2) or (len(list_a) == 3 and len(list_c) == 2):
        return True
    elif (len(list_b) == 3 and len(list_a) == 2) or (len(list_b) == 3 and len(list_c) == 2):
        return True
    elif (len(list_c) == 3 and len(list_a) == 2) or (len(list_c) == 3 and len(list_b) == 2):
        return True
    else:
      return False