"""
This program has a menu that gives the user three options of functions to run.
The first function is a poem generator,
The second function is a squared product generator,
And the third function is a CAD to YUAN translator.
Author:  Benjamin Hilderman
Student Number: 20374738
Date:  Oct 7, 2022
"""
import random

def poemGenerator(name1, name2, name3, name4, name5, name6, name7, name8):
    """
    This function gets 8 parameters, name1, name2, name3, name4, name5, name6, name7, name8, prints a poem with one of the parameters.
    Parameters: name1, name2, name3, name4, name5, name6, name7, name8 - strings representing first names
    Print Value - a poem using a randomely chosen name
    """
    arrayOfNames = [name1, name2, name3, name4, name5, name6, name7, name8]
    print('Loops were crazy, \nWhat are functions about?\n' + random.choice(arrayOfNames) + ', you can do this \nJust stick it out!')

def squaredProduct(n, m):
    """
    This function takes two integers as parameters, n and m and returns the product of the square of each of the values from n to m 
    Parameters:  n, m - integer values representing the range of the numbers that get squared
    Return Value - the value of the squared numbers - an integer 
    """
    squared = 1
    if 0 < m - n < 4:
        while n <= m:
            squared *= n * n
            n += 1
        return int(squared)
    else: return 0

def cadToYuanTranslator(n):
    """
    This function multiplies the parameter by 5.19, n, and returns the result.
    Parameters:  n - integer value representing CAD
    Return Value - the total of n multiplied by 5.19 - a float value
    """
    yuan = round(n * 5.19, 2)
    return yuan

def menu():
    """
    This function is a menu. This gets the user's input and runs the corresponding function. This function ends when the user's input isn't 1, 2, or 3
    """
    menuLoop = 'loop'
    while menuLoop == 'loop':
        userChoice = input('There are three functions you can run:\n(1) The poem generator\n(2) The squared product generator between two values\n(3) The CAD to YUAN convertor\nOr input anything else to quit\n')
        if userChoice == '1':
            poemGenerator("Adam", "Ava", "Alex", "Aaron", "Ben", "Brianna", "Carl", "Dan")
        elif userChoice == '2':
            n = float(input('Enter the first value: '))
            m = float(input('Enter the second value (must be 1-3 higher than the first value): '))
            totalNumber = squaredProduct(n, m)
            print(totalNumber)
        elif userChoice == '3':
            cad = float(input('Enter a value in CAD to get the YUAN conversion: '))
            yuanTotal = cadToYuanTranslator(cad)
            print(yuanTotal)
        else: 
            print('You quit')
            menuLoop = 'end'
menu()