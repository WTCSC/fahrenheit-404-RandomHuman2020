from os import environ
import time
import progressbar

willrestart = True

print(f"Welcome to Fahrenheit 404, {environ.get('USER')}.")
print("Loading...")
b = progressbar.ProgressBar(maxval=100)
b.start()
for i in range(100):
    time.sleep(0.03)
    b.update(i + 1)
b.finish()
while willrestart:
    print("Please select the units you would like to convert.\n")
    units = input("Press 1 for Fahrenheit -> Celcius \n\nPress 2 for Celcius -> Fahrenheit \n\nPress 3 for Kelvin -> Fahrenheit \n\nPress 4 for Kelvin -> Celsius\n\nPress 5 for Fahrenheit -> Kelvin\n\nPress 6 for Celsius -> Kelvin\n\n ----------- \n")

    if units == "1":

        inunitstr = "Fahrenheit"
        outunitstr = "Celsius"
    elif units == "2":
        inunitstr = "Celsius"
        outunitstr = "Fahrenheit"
    elif units == "3":
        inunitstr = "Kelvin"
        outunitstr = "Fahrenheit"
    elif units == "4":
        inunitstr = "Kelvin"
        outunitstr = "Celsius"
    elif units == "5":
        inunitstr = "Fahrenheit"
        outunitstr = "Kelvin"
    elif units == "6":
        inunitstr = "Celsius"
        outunitstr = "Kelvin"
    else:
        print("Invalid selection. Quitting...")
        exit(42)

    intemp = input(f"Type the temperature you would like to convert to {outunitstr}: ")

    try:
        intemp = float(intemp)
        if units == "2" and intemp < -274 or intemp > 9999:
            print("Invalid temperature. Restarting...")
        elif units == "1" and intemp < -460 or intemp > 9999:
            print("Invalid temperature. Restarting...")
        elif units == "3" and intemp < 0 or intemp > 9999:
            print("Invalid temperature. Restarting...")
        elif units == "4" and intemp < 0 or intemp > 9999:
            print("Invalid temperature. Restarting...")
        elif units == "5" and intemp < -460 or intemp > 9999:
            print("Invalid temperature. Restarting...")
        elif units == "6" and intemp < -274 or intemp > 9999:
            print("Invalid temperature. Restarting...")
        else:
            if units == "1":
                outtemp = (intemp - 32) * 0.555

            elif units == "2":
                outtemp = (intemp * 1.8) + 32
            elif units == "3":
                outtemp = (intemp * 1.8) + 459.67
            elif units == "4":
                outtemp = intemp - 273.15
            elif units == "5":
                outtemp = (intemp + 459.67) / 1.8
            elif units == "6":
                outtemp = intemp + 273.15
            print(f"\n{intemp} degrees {inunitstr} is equal to {str(round(outtemp, 2))} degrees {outunitstr}.")
            restarting = input("Do you want to convert more? ")
            if restarting.lower() == "yes" or restarting.lower() == "y":
                willrestart = True
            else:
                willrestart = False

    except ValueError:
        print("Invalid temperature. Restarting...")
        exit(1)

