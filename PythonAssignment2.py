#Assignment 2
-------------
# Check the Number is Even or odd
def checkEvenOdd():
    vNum = int(input("Enter the Number to check Even or Odd "))
    if vNum % 2 == 0:
        print(vNum , " is Even Number ")
    else:
        print(vNum, " is Odd Number")
        
checkEvenOdd() 

# Get Sum of numbers from range 1 to 50
def calculateSum():
    total = 0
    for i in range(1,50):
        total = total + i
    print(total)
        
calculateSum() 

# 2nd method, Get Sum of numbers from range 1 to 50
def calculateSum():
    for i in range(1,50):
        total = sum(range(1, i+1))
    print(total)
        
calculateSum()