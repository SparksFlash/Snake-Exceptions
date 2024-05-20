try:
    file = open("CleaningUp.py")
    age = int(input("Age :"))
    xfactor = 10 / age

except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
# except ZeroDivisionError:
#     print("Age can not be 0.")
else:
    print("No exceptions were thrown.")
finally:
    file.close
