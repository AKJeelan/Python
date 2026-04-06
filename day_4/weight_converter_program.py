weight = input("Weight: ")
weight = float(weight)

unit = input("(L)bs or (K)g: ")
unit = unit.lower();

if unit == 'k':
    print(f"You are {weight / 0.45} pounds")
elif unit == 'l':
    print(f"You are {weight * 0.45} kgs")