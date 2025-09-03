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
    units = input("Press 1 for Fahrenheit -> Celcius \n\nPress 2 for Celcius -> Fahrenheit \n\n ----------- \n")

    if units == "1":

        inunitstr = "Fahrenheit"
        outunitstr = "Celsius"
    elif units == "2":
        inunitstr = "Celcius"
        outunitstr = "Fahrenheit"
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
        else:
            if units == "1":
                outtemp = (intemp - 32) * 0.555

            elif units == "2":
                outtemp = (intemp * 1.8) + 32
            print(f"\n{intemp} degrees {inunitstr} is equal to {outtemp} degrees {outunitstr}.")
            restarting = input("Do you want to convert more? ")
            if restarting == "yes" or restarting == "y" or restarting == "Y" or restarting == "Yes":
                willrestart = True
            else:
                willrestart = False

    except ValueError:
        print("Invalid temperature. Restarting...")
        exit(1)

