# With
try:
    with open("CleaningUp.py") as file:
        print("File opened.")
    age = int(input("Age :"))
    xfactor = 10 / age

except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
# except ZeroDivisionError:
#     print("Age can not be 0.")
else:
    print("No exceptions were thrown.")

    # Raising now
