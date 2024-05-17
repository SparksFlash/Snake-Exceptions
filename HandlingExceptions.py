try:
    age = int(input("Age :"))
    xfactor = 10 / age

except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
except ZeroDivisionError:
    print("Age can not be 0.")
else:
    print("No exceptions were thrown.")
print("Execution continues.")
