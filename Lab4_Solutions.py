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

#Problem 3
#Jose Carrizales
#CSE 5408

def toMilitaryTime(string):
    # Once we hit midnight we will reset to 0:00 and the new set of 24 hours begins
    if(string[-2:] == "AM" and string[:2] == "12"):
        return "00" + string[2:-2]

    # If its not 12:00 AM we will keep the time we have but remove the AM from it
    elif string[-2:] == "AM":
        return string[:-2]

    # If the time is 12:00 PM we don't have to do anything but remove the PM
    elif (string[-2:] == "PM" and string[:2] == "12"):
        return string[:-2]

    # Any other time after 12:00 PM we will add 12 to it so that we know the time converted to 24 hours
    else:
        newString = str(int(string[:2]) + 12) + string[2:-2]
        return newString
