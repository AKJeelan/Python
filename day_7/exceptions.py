try:
    age = int(input("age: "))
    print(age)
    age / 0
except ValueError:
    print("Please enter a valid input")
except ZeroDivisionError:
    print("Can't be divided")

