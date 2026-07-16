# Max_Gomez

# Function to calculate total wages before taxes
def Calculatewages(wage, hours):
    wagetotal = hours * wage
    return wagetotal


# Function to calculate federal tax based on marital status
def CalcualteFederaltax(wagetotal, mstatus):
    if mstatus == "Married":
        fedtax = wagetotal * 0.20
    elif mstatus == "Single":
        fedtax = wagetotal * 0.25
    else:
        fedtax = wagetotal * 0.22

    return fedtax


# Function to calculate state tax based on state of residence
def calculateStatetax(wagetotal, residence):
    if (
        residence == "CA"
        or residence == "NV"
        or residence == "SD"
        or residence == "WA"
        or residence == "AZ"
    ):
        statetax = wagetotal * 0.08

    elif (
        residence == "TX"
        or residence == "IL"
        or residence == "MO"
        or residence == "OH"
        or residence == "VA"
    ):
        statetax = wagetotal * 0.07

    elif (
        residence == "NM"
        or residence == "OR"
        or residence == "IN"
    ):
        statetax = wagetotal * 0.06

    else:
        statetax = wagetotal * 0.05

    return statetax


# Function to calculate wages after taxes
def calcualtenet(wagetotal, fedtax, statetax):
    netwages = wagetotal - fedtax - statetax
    return netwages


# Main body
hours = int(input("Please enter your work hours: \n"))
wage = int(input("Please enter your hourly rate: \n"))
residence = input("Please enter your state of residence: \n")
mstatus = input("Please enter your marital status: \n")

print("**********")

result1 = Calculatewages(wage, hours)
result2 = CalcualteFederaltax(result1, mstatus)
result3 = calculateStatetax(result1, residence)
result4 = calcualtenet(result1, result2, result3)

print("Your wage is: $" + str(result1))
print("Your federal tax is: $" + str(result2))
print("Your state tax is: $" + str(result3))
print("Your net wage is: $" + str(result4))
print("**********")
