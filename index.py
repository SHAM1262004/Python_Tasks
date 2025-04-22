#Find Palindrome word

def Palindrome():
    word,word2 = input("Enter your word: "),''

    for i in word:
        word2 = i + word2

    if word == word2 : print("The given word is palindrome") 
    else: print("The given number is not palindrome")
Palindrome()

#Find largest number and smallest number in the array

def Largesmall():
    numlist = [100,103,99,121,150,10,30,151,50]
    largest,smallest = numlist[0],numlist[0]

    for i in range(0,len(numlist)):
        if numlist[i] > largest or numlist[i] < smallest :
           if numlist[i] > largest:
                 largest = numlist[i]
           elif numlist[i] < smallest:
                 smallest = numlist[i]

    print(f'The largest number is {largest}')
    print(f'The smallest number is {smallest}')
Largesmall()

# Fill the  missing numbers inbetween the list

def Missing():
    numbers = [0,2,4,6,8,10,20]
    for i in range(numbers[0],numbers[-1]):
        if i not in numbers:
            numbers.insert(i,i)
    print(numbers)
Missing()

#Find the given number is odd or even

def Oddeven():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print('The given number is even number')

    else :
        print('The given number is odd number')
Oddeven()

#Find a factorial of given number

def Factorial():
    number = int(input('Enter a number: '))
    number2 = 1
    while number > 1:
        number2 = number*number2
        number -= 1

    print(f'The factorial of given number is: {number2}')
Factorial()

#Remove duplicates in the list

def Duplicate():
    numbers = [10,20,5,6,10,25,72,81,5,91,97,6,20,8,1,6,11,10]
    numbers2 = []
    for i in range(0,len(numbers)):
        if numbers[i] not in numbers2:
            numbers2.append(numbers[i])
    print(numbers2)

Duplicate()

#Display the given numbers table

def Tables():
    table = int(input('Enter a number: '))
    for i in range(1,10+1):
        print(f'{table} * {i} = {table*i}')
Tables()

#Find the given number is a amstrong or not

def Amstrong():
    number = int(input('Enter a number: '))
    strnum = str(number)
    lenofnum = len(strnum)
    
    total = 0
    
    for i in strnum:
        total += int(i) ** lenofnum
        
    print('The given number is amstrong') if number == total else print('The given number is not amstrong')
        
    print(total)
    
Amstrong()

# #Triangle pattern

def Triangle():
    number = int(input('Enter a number: '))

    for i in range(1,number):
        for j in range(number-1,i,-1):
            print(' ',end='')
        for k in range(0,i):
            print('*',end=' ')
        print()
    
Triangle()

#Dimond pattern

def Dimond():
    number = int(input('Enter a number: '))

    for i in range(1,number):
        for j in range(number-1,i,-1):
            print(' ',end='')
        for k in range(0,i):
            print('*',end=' ')
        print()
    for i in range(1,number):
        for k in range(0,i):
            print(' ',end='')
        for j in range(number-1,i,-1):
            print('*',end=' ')
        print()
        
Dimond()
