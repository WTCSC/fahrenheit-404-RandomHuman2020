from os import environ

print(f"Welcome to Fahrenheit 404, {environ.get('USER')}.")
print("Please select the units you would like to convert.\n")
units = input("Press 1 for Fahrenheit -> Celcius \n\nPress 2 for Celcius -> Fahrenheit \n\n ----------- \n")

if units == "1":

    inunitstr = "Celcius"
    outunitstr = "Fahrenheit"
elif units == "2":
    inunitstr = "Fahrenheit"
    outunitstr = "Celcius"
else:
    print("Invalid selection. Quitting...")
    exit(1)

intemp = input(f"Type the temperature you would like to convert to {inunitstr}: ")

try:
    intemp = float(intemp)
    if units == "1":
        outtemp = (intemp - 32) * 0.5555
    elif units == "2":
        outtemp = (intemp * 1.8) + 32
    print(f"{intemp} degrees {inunitstr} is equal to {outtemp} degrees {outunitstr}.")
except ValueError:
    print("Invalid temperature. Quitting...")
    exit(1)
