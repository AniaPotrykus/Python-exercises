#Your task is very simple. Just write a function that takes an input string of lowercase letters and returns true/false depending on 
#whether the string is in alphabetical order or not.

#Examples (input -> output)
#"kata" -> false ('a' comes after 'k')
#"ant" -> true (all characters are in alphabetical order)

def alphabetic(s):
    new_s = sorted(s)
    if s == new_s:
        return True
    else:
        return False