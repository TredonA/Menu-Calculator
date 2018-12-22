# Menu Calculator | by Trey Austin
# Simple menu print out and total calculator for the workers that require
# a quick working program to aid them in their customer interactions.

from math import floor

def totalCalculator(employeeInput):
    numChickenStrips = 0;
    numFrenchFries = 0;
    numHamburgers = 0;
    numHotdogs = 0;
    numLargeDrinks = 0;
    numMediumDrinks = 0;
    numMilkShakes = 0;
    numSalads = 0;
    numSmallDrinks = 0;
    i = 0;
    totalPrice = 0;
    while i < len(employeeInput):
        if employeeInput[i] == '1':
            totalPrice += 3.50
            numChickenStrips += 1
        elif employeeInput[i] == '2':
            totalPrice += 2.50
            numFrenchFries += 1
        elif employeeInput[i] == '3':
            totalPrice += 4.00
            numHamburgers += 1
        elif employeeInput[i] == '4':
            totalPrice += 3.50
            numHotdogs += 1
        elif employeeInput[i] == '5':
            totalPrice += 1.75
            numLargeDrinks += 1
        elif employeeInput[i] == '6':
            totalPrice += 1.50
            numMediumDrinks += 1
        elif employeeInput[i] == '7':
            totalPrice += 2.25
            numMilkShakes += 1
        elif employeeInput[i] == '8':
            totalPrice += 3.75
            numSalads += 1
        else:
            totalPrice += 1.25
            numSmallDrinks += 1
        i += 1
    print("You have ordered: ")
    if(numChickenStrips > 0):
        print(str(numChickenStrips) + " order of Chicken Strips")
    if(numFrenchFries > 0):
        print(str(numFrenchFries) + " order of French Fries")
    if(numHamburgers > 0):
        if(numHamburgers == 1):
            print(str(numHamburgers) + " Hamburger")
        else:
            print(str(numHamburgers) + " Hamburgers")
    if(numHotdogs > 0):
        if(numHotdogs == 1):
            print(str(numHotdogs) + " Hotdog")
        else:
            print(str(numHotdogs) + " Hotdogs")
    if(numLargeDrinks > 0):
        if(numLargeDrinks == 1):
            print(str(numLargeDrinks) + " Large Drink")
        else:
            print(str(numLargeDrinks) + " Large Drinks")
    if(numMediumDrinks > 0):
        if(numMediumDrinks == 1):
            print(str(numMediumDrinks) + " Medium Drink")
        else:
            print(str(numMediumDrinks) + " Medium Drinks")
    if(numMilkShakes > 0):
        if(numMilkShakes == 1):
            print(str(numMilkShakes) + " Milkshake")
        else:
            print(str(numMilkShakes) + " Milkshakes")
    if(numSalads > 0):
        if(numSalads == 1):
            print(str(numSalads) + " Salad")
        else:
            print(str(numSalads) + " Salads")
    if(numSmallDrinks > 0):
        if(numSmallDrinks == 1):
            print(str(numSmallDrinks) + " Small Drink")
        else:
            print(str(numSmallDrinks) + " Small Drinks")
    if totalPrice % (floor(totalPrice)) == .0 or \
    totalPrice % (floor(totalPrice)) == .5:
        print("This will come out to a total of $" + str(totalPrice) + "0")
    else:
        print("This will come out to a total of $" + 
              str(totalPrice))
    userCmd = input("Thank you for using the program. Would you" + 
          " like to go again? Please type in Y or to use again or N to exit: ")
    if(userCmd == 'N' or userCmd == 'n'):
        print("Thank you for using the Diner Aid. Have a good day!")
    elif(userCmd == 'Y' or userCmd == 'y'):
        newInput = input("Please enter a new order: ")
        inputChecker(newInput)
    else:
        print("Unrecognized input. Exiting program now...")

def inputChecker(employeeInput):
    try:
        int(employeeInput)
    except:
        newInput = input("Input was invalid! Please try again and make sure " +
                         "that you're only entering integer values: ")
        inputChecker(newInput)
    else: 
        totalCalculator(employeeInput)


itemsPurchased = input("\'Trey's Diner Aid\' for employees. Here are the" +
    " numbers for each menu item:\n 1. Chicken Strips\n 2. French Fries\n" +
    " 3. Hamburger\n 4. Hotdog\n 5. Large Drink\n" +
    " 6. Medium Drink\n 7. Milk Shake\n 8. Salad\n 9. Small Drink\n" +
    "Please feel free to enter the numbers of the menu items that" +
    " are being purchased: ")
inputChecker(itemsPurchased)
