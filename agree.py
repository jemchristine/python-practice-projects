x = input ("Do you agree? Y/N: ")
x = x.lower()

#if x == "Y" or x == "y":
#if x in ["Y", "y"]:
if x in ["yes", "y"]:
    print("Agreed")
#elif x == "N" or x == "n":
#elif x in ["N", "n"]:
elif x in ["no", "n"]:
    print("Not Agreed")
else:
    print("Please enter Y/N")



