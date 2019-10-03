import random

text_str = input("Type the text to be scrambled and hit enter:")
print(text_str)

#split string by the space character into a list
list = text_str.split()
type(list)

#iterate over all words in the list and scramble each of them
#don't forget to check for punctuation marks
i=0
j=0
length=0
temp1=0
temp2=0
new=0
switch=0

result = ""

#Goes through each word in the list
while j < len(list):
    i = list[j]
    temp1 = i[0]
    p=len(i)
    p=p-1
    temp2 = i[p]
    ''.join(random.sample(i, len(i)))
    #scrambles up the word
    while len(i) >= length:
        if i[length] == temp1:
            switch = i[0]
            i[0] = temp1
            i[length] = switch
        if i[length] == temp2:
            switch = i[p]
            i[p] = temp2
            i[length] = switch
        print(i)
        length = length + 1

    j=j+1

#print new list with scrambled words

