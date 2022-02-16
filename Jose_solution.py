#

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


# We can add seconds if needed, the code has been optimized for it
print(toMilitaryTime("12:00AM"))
print(toMilitaryTime("12:00PM"))
print(toMilitaryTime("09:30AM"))
print(toMilitaryTime("09:30PM"))
