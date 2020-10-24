# -*- coding: utf-8 -*-
"""
Write a program that reads a string and displays the appropriate messages, 
The programs must check if:
a. contains only letters
b. contains only uppercase letters
c. contains only lowercase letters
d. contains only digits
is. it contains only letters and numbers
f. starts with a capital letter
"""


# Return True if there are only numbers inside the string
def containsNumbers (str):
    numbers = "0123456789"
    counter = 0
    for letter in str:
        for n in numbers:
            if letter == n:
                counter = counter + 1
    return (counter == len(str))

# Return True if there are only letters inside the string
def containsLetters (str):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    counter = 0
    for letter in str:
        for alphaLetter in alphabet:
            if letter == alphaLetter:
                counter = counter + 1 
    return (counter == len(str))

# Return True if there are only Upper letters inside the string
def containsUpperLetters (str):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = 0
    for letter in str:
        for alphaLetter in alphabet:
            if letter == alphaLetter:
                counter = counter + 1      
    return (counter == len(str))

# Return True if there are only Lower Letters inside the string
def containsLowerLetters (str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    counter = 0
    for letter in str:
        for alphaLetter in alphabet:
            if letter == alphaLetter:
                counter = counter + 1
    return (counter == len(str))

# Return True if there are only Numbers and Letters inside the string
def containsNumberAndLetters (str): 
    return containsNumbers(str) == containsLetters(str)

# Return True if the string starts with an Uuppercase
def startsWithUpperCase (str):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in alphabet:
        if letter == str[0]:
            return True
    return False
        
str = input("Enter a word:")

# Calling the functions
print("The string contains only numbers:", containsNumbers(str))
print("The string contains only letters:", containsLetters(str))
print("The string contains only lower letters:", containsLowerLetters(str))
print("The string contains only upper letters:", containsUpperLetters(str))
print("The string contains numbers and letters:", containsNumberAndLetters(str))
print("The string starts with an uppercase:", startsWithUpperCase(str))
    


