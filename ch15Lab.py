'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''


import re
# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


file = open("dictionary.txt", "r")
dict_list = []
for line in file:
    dict_list.append(line.strip())
print(dict_list)


file.close()

print("---LINEAR SEARCH---")
file = open("AliceInWonderLand.txt", "r")

wrong = []
line_number = 0
for line in file:
    line_number += 1
    words = split_line(line)
    #print(words)
    for word in words:
        #print(word)
        key = word.upper()
        #print(key)
        #i = 0
        for i in range(len(dict_list)):
            if dict_list[i] == key:
                break
        else:
            print(key, "on line", line_number, "is not a word")


        #while i < len(dict_list) and dict_list[i] == key:
         #   i += 1
        #if dict_list[i] != key:
         #   wrong.append(key)



print("---Binary Search---")
line_number = 0
for line in file:
    line_number += 1
    words = split_line(line)
    #print(words)
    for word in words:
        #print(word)
        key = word.upper()
        lower_bound = 0
        upper_bound = len(dict_list) - 1
        found = False
        while lower_bound <= upper_bound and not found:
            middle = (lower_bound + upper_bound) // 2
            if dict_list[middle] < key:
                lower_bound = middle + 1
            elif dict_list[middle] > key:
                upper_bound = middle - 1
            else:
                found = True
        #if found:
         #print("found", key, "at position", middle)
        if not found:
            print(key, "on line", line_number, "is not a word")

file.close()



