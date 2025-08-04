# Assignment 3
# Functions and Modules in Python
# 1. Calculate Factorial Using a Function
def getFactorial():
    vNum = int(input("Enter the number for factorial "))
    for i in range(1, vNum):
        #print(i)
        total = sum(range(1, i+1))
    print(total)
        
getFactorial()


# 2. Using the Math Module for Calculations
import math

def getMathValues():
    print("Welcome for calculation of\n 1. Square Root Number\n 2. Natural logarithm\n 3. Sine of the number (in radians)")
    vNum = int(input("Enter the Number "))
    
    print("The results are\n")
    print(f"The Square root for {vNum} is ", vNum*vNum)
    print(f"The Natural logarithm for {vNum} is ", math.log(vNum))
    print(f"The Sine of the number (in radians) for {vNum} is ", math.sin(vNum))
    
    
getMathValues()       