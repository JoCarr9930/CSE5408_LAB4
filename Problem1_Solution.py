#Brian Saldana
#CSE 5408 
#Lab 4
#Problem 1: Write a program containing a function to reverse a user inputted string.

def Reverse(x):
    return x[::-1]

x = input("Enter a String !\n")
print("This is your String Reversed!\n"+ Reverse(x))

