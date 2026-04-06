# temprature = input('Enter the temprature : ')
# temprature = float(temprature)

# if temprature > 30:
#     print("it's a hot day")
# elif temprature < 10:
#     print("it's a cold day")
# else:
#     print("it's neither hot or cold")

name = input("Enter your name : ")
name_length = len(name)

if name_length < 3:
    print("name must be atleast 3 characters")
elif name_length > 50:
    print("name must be atleast 50 characters")
else:
    print("name looks good!")

