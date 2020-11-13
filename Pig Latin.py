#Creating Pig Latin

# Creating the pig_latin function

X =['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    for i in word:
        #if isVowel(i) == True:
            print(vowel(word))
    else:
        print(consonats(word,i))

def isVowel(firstLetter):
    for j in x:
        if j is firstLetter:
            return True

def vowel(alpha):
    return alpha + 'ay'

def consonats(alpha,firstLetter):
    y = alpha + firstLetter + 'ay'
    return y[1::]

pig_latin('victor')


# importing the random function

import random

def roll_dice(sides, rolls):
    for _ in range(rolls):
        print (random.randint(1, sides))
    print("That's all")

roll_dice(6,3)

# creating the is_palindrome function

def is_palindrome(enter_string):
    new_string = ""
    reverse_string = ""
    
    for word in enter_string:
        word = word.lower()
        if word != " ":
            new_string = new_string + word
            reverse_string = word + reverse_string
   
    if new_string == reverse_string:
        return True
    return False

print(is_palindrome("Meme"))


