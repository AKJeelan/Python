# int() --> use to convert values to integer
# float() --> use to convert values to floating / decimal points
# bool() --> use to convert values to boolean
# type() --> use to know the type of variable

weight_lbs = input('Enter your weight in pounds : ')
weight_kg = float(weight_lbs) * 0.45

print(weight_kg)

print(type(weight_lbs))
print(type(weight_kg))

