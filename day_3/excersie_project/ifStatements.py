# Price of a house is $1M.

# If buyer has good credit,
# they need to put down 10%.

# Otherwise
# they need to put down 20%.

# Print the down payment


is_good_credit = False
print("Price of house is $1M")

if is_good_credit:
    print("Congratulations!, you have a good credit.")
    print(f"you need to pay 10% Down payment which is : ${1 * 0.1}M ")
else:
    print(f"Congratulations! you need to pay 20% Down payment which is : ${1 * 0.2}M ")