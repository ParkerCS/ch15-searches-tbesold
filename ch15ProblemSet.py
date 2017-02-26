'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''

#1.  (7pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.

file = open("dictionary.txt", "r")

#word_list = []
long = " "
x = 0

for line in file:
    if len(line) >= x:
        x = len(line)
        long = line
print(x)
print(long)
file.close()

#2.  (10pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"


import re
def split_line(line):
    #This function takes in a line of text and returns a list of words in the line
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open("AliceInWonderLand.txt", "r")


words = 0
length = []
for line in file:
    word = split_line(line)
    #print(word)
    for i in range(len(word)):
        words += 1
    for abc in word:
        #print(abc)
        length.append(len(abc))
        total = sum(length)
        avg = total/words

#print(length)
print("the avergae word length in Alice in Wonderland is", avg, "letters")
print("there are", words, "words in Alice and Wonderland" )

file.close()
# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?


#### OR #####

#3  (13pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"

import re
def split_line(line):
    #This function takes in a line of text and returns a list of words in the line
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

seven_list = []
file = open("AliceInWonderLand.txt", "r")
for line in file:
    word = split_line(line)
    for seven in word:
        if len(seven) == 7:
            seven_list.append(seven)

#print(seven_list)

from collections import Counter    #looked this part up
count = Counter(seven_list)
print(count)
print("'herself' is the most common 7 letter word in Alice n Wonderland. It occurs 83 times")

# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.



