#Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

#Examples
#"the-stealth-warrior" gets converted to "theStealthWarrior"

#"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

#"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

import re

def to_camel_case(text):
    
    result = []
    no_dashes = re.sub("(_|-)", " ", text)
    word_list = no_dashes.split()
    
    for i, word in enumerate(word_list):
        if i == 0:
            result.append(word)
        else:
            result.append(word.capitalize())
        
    return "".join(result)
