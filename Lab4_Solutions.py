# Group 1
# Jose Carrizales
# Brian Saldana
# Jason Galicia

# CSE 5408
# Spring 2022
# Lab 4

#Brian Saldana
#CSE 5408 
#Lab 4
#Problem 1: Write a program containing a function to reverse a user inputted string.

def Reverse(x):
    return x[::-1]

x = input("Enter a String !\n")
print("This is your String Reversed!\n"+ Reverse(x))

#Problem 2
#Jason Galicia
#CSE 5408
#Problem2.py

def checkprime(int1):
    #checks if number is greater than one
    if int1 > 1:

        #Starts loop to go from the range of 2 to int1 which is the user input
        for i in range(2,int1):
            #Does the modulus of the int1 and i which if is  = to 0 then it is not prime
            if (int1 % i) == 0:
                print(int1, "is not a prime member")
                break
        #If it is not equal to zero then it is a prime number and it will print out
        else:
            print(int1, "is a prime number")
    #If it is less then 1 then it will print out that it is not a prime number
    else:
        print(int1, "is not a prime number")

#This gets the user input and puts it into number
number = int(input("Enter a number to check if prime: "))

#Calls checkprime and see if it is a prime number or not
checkprime(number)