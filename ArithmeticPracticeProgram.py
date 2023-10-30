# Practice Program
import random

name = input("What is your name? ")
print("Welcome, " + name + "!")

#Practice Functions below -------------------------------------

#Multipication in order
def multiplyInOrder(minRange, rangeNum):
    print("We will be practicing multipication problems, " + str(minRange) + " - " + str(rangeNum))
    score = 0
    for i in range(1, rangeNum + 1):
        for j in range(minRange, rangeNum + 1):
            while True:
                try:
                    answer = int(input(str(i) + " x " + str(j) + " = "))
                except ValueError:
                    print("I didn't understand, please try again")
                else:
                    break
            if (answer == i * j):
                score = score + 1
            else :
                print("The correct answer is " + str(j * i))
            
    printScore(score, (rangeNum*rangeNum))
    
#Multipication with random integers
def multiplyRandInt(rangeNum):
    print("We will be practicing random multipication problems")
    score = 0
    for i in range(1, rangeNum + 1):
        randInt = random.randint(1, rangeNum)
        while True:
            try:
                answer = int(input(str(i) + " x " + str(randInt) + " = "))
            except ValueError:
                print("I didn't understand, please try again")
            else:
                break
        if (answer == i * randInt):
            score = score + 1
        else :
            print("The correct answer is " + str(randInt * i))
            
    printScore(score, rangeNum)
    
#Practice multiplying a number
def multiplyFocusOnly(rangeNum, focusNum):
    score = 0
    for i in range(1, rangeNum + 1):
        while True:
                try:
                    answer = int(input(str(focusNum) + " x " + str(i) + " = "))
                except ValueError:
                    print("I didn't understand, please try again")
                else:
                    break
        if (answer == focusNum * i):
            score = score + 1
        else :
            print("The correct answer is " + str(focusNum * i))

    printScore(score, (rangeNum*rangeNum))
    
#Multipication with a fixed value * random integers
def multiplyFocusTimesRandInt(rangeNum, focusNum):
    print("We will be practicing " + str(focusNum) + " * random numbers")
    score = 0
    for i in range(1, rangeNum + 1):
        randInt = random.randint(1, rangeNum)
        while True:
            try:
                answer = int(input(str(focusNum) + " x " + str(randInt) + " = "))
            except ValueError:
                print("I didn't understand, please try again")
            else:
                break
        if (answer == focusNum * randInt):
            score = score + 1
        else :
            print("The correct answer is " + str(randInt * focusNum))
            
    printScore(score, rangeNum)
    
#Multipication with evens - rangeNum, X evens
def multiplyEvens(rangeNum):
    print("We will be practicing multiplying even numbers, 1 - " + str(rangeNum))
    score = 0
    for i in range(1, rangeNum + 1):
        for j in range(2, rangeNum + 1, 2):
            while True:
                try:
                    answer = int(input(str(i) + " x " + str(j) + " = "))
                except ValueError:
                    print("I didn't understand, please try again")
                else:
                    break
            if (answer == i * j):
                score = score + 1
            else:
                print("The correct answer is " + str(i * j))
            
    printScore(score, (rangeNum * int(rangeNum/2)))
    
#Multipication with odds - rangeNum, X odds
def multiplyOdds(rangeNum):
    print("We will be practicing multiplying even numbers, 1 - " + str(rangeNum))
    score = 0
    for i in range(1, rangeNum + 1):
        for j in range(1, rangeNum + 1):
            if (j % 2 != 0):
                while True:
                    try:
                        answer = int(input(str(i) + " x " + str(j) + " = "))
                    except ValueError:
                        print("I didn't understand, please try again")
                    else:
                        break
                if (answer == i * j):
                    score = score + 1
                else :
                    print("The correct answer is " + str(j * i))
        
    printScore(score, (rangeNum * int((rangeNum + 1)/2)))    

#Division in order
def divisionInOrder(divRange):
    answer = 0
    scoreMinus = 0
    qNum = 0
    print("We will be practicing division problems, 1 - " + str(divRange))

    for i in range(1, divRange + 1):
        for j in range(1, divRange + 1):
            while True:
                try:
                    #A way to find the divisible numbers and then get the input
                    if i % j == 0:
                        qNum = qNum + 1
                        key = i/j
                        while (answer != key):
                            answer = int(input(str(i) + " / " + str(j) + " = "))
                            if (answer != key):
                                scoreMinus = scoreMinus + 1
                                print("Try again")
                            
                except ValueError:
                    print("I didn't understand, please try again")
                else:
                    break
    
    printScore(qNum - scoreMinus, qNum)
    
#Multiplication && Divison 
def multDivPrime(rangeNum):
    score = 0
    probNum = 0
    for i in range(1, rangeNum + 1):
        #Restart prime check
        primeCheck = 0
        for j in range(1, rangeNum + 1):
            #Mult Problem (within j loop)
            probNum = probNum + 1
            while True:
                try:
                    answer = int(input(str(i) + " x " + str(j) + " = "))
                except ValueError:
                    print("I didn't understand, please try again")
                else:
                    break
            if (answer == i * j):
                score = score + 1
            else :
                print("The correct answer is " + str(j * i))
        #Restart j loop for division questions
        #Div Problem (within j loop)
        for j in range(1, rangeNum + 1):
            if (i % j == 0):
                primeCheck = primeCheck + 1
                probNum = probNum + 1
                while True:
                    try:
                        answer = int(input(str(i) + " / " + str(j) + " = "))
                    except ValueError:
                        print("I didn't understand, please try again")
                    else:
                        break
                if (answer == i / j):
                    score = score + 1
                else :
                    print("The correct answer is " + str(int(i / j)))
        #Prime Question (after j loop but within i loop)
        probNum = probNum + 1
        while True:
            try:
                answer = int(input("Is " + str(i) + " a prime number? Type 0 for No || 1 for Yes: "))
            except ValueError:
                print("I didn't understand, please try again")
            else:
                break
        if (primeCheck == 2):
            if (answer == 1):
                score = score + 1
            else :
                print("The correct answer is 1")
        else :
            if (answer == 0):
                score = score + 1
            else :
                print("The correct answer is 0")
    
    printScore(score, probNum)
    
def squarePractice(rangeNum):
    print("We will be practicing the square of numbers 1 - " + str(rangeNum))
    score = 0
    for i in range(1, rangeNum + 1):
        while True:
            try:
                answer = int(input(str(i) + " x " + str(i) + " = "))
            except ValueError:
                print("I didn't understand, please try again")
            else:
                break
        if (answer == i * i):
            score = score + 1
        else :
            print("The correct answer is " + str(i * i))
            
    printScore(score, rangeNum)
    
        
    
#Output score details
def printScore(score, probNum):
    print(name + ", you scored a " + str(score) + " out of " + str(probNum) + "!")
    percent = (score * 100) / (probNum)
    print("That is " + str(int(percent)) + "%!")
 
 
# Calls to functions ----------------------------------------------

''' 
Functions consist of 
- Multiply (numbers from 1 -> rangeNum) * (numbers from minRange -> rangeNum) Time complexity: O(rangeNum * (minRange * rangeNum))
multiplyInOrder(minRange, rangeNum)

- Multiply (numbers 1 to rangeNum) * (random numbers ranging from (1 -> rangeNum)) Time complexity: O(n)
multiplyRandInt(rangeNum)

- Multiply (focus number) * (numbers from 1 -> rangeNum) Time complexity: O(n)
multiplyFocusTimesRandInt

- Multiply (focus number) * (random numbers ranging from (1 -> rangeNum)) for number of rangeNum iterations. Time complexity: O(n)
multiplyFocusTimesRandInt(rangeNum, focusNum)

- Multiply (numbers from 1 -> rangeNum) * (even numbers starting from 2 -> rangeNum). Time complexity: O(n * (n/2)) == O(n)
multiplyEvens(rangeNum)

- Multiply (numbers from 1 -> rangeNum) * (odd numbers starting from 1 -> rangeNum). Time complexity: O(n * (n/2)) == O(n)
multiplyOdds(rangeNum)

- Divide (current = all numbers from 1 -> divRange) / (all numbers that are divisible by the current number, starting from 1 until divRange)
divisionInOrder(divRange)

- Multiply (numbers from 1 -> rangeNum) * (numbers from 1 -> rangeNum). Then divide (numbers from 1 -> rangeNum) / (numbers from 1 -> rangeNum).
Then answer the question, is the current number a prime number?
multDivPrime(rangeNum)

- Determine the square of all numbers from 1 -> rangeNum
squarePractice(rangeNum)
'''