import converters
import utils
# from Day_6.listes import numbers
from converters import kg_to_lbs
from ecommerce import shipping

# print(kg_to_lbs(100))
# print(converters.lbs_to_kg(70))

# result = utils.findMax(numbers)
# print(result)
# print(max(numbers))

# Why it prints 3 times:
#
# • Importing a file runs all its code
# • `listes.py` has a print statement → runs during import
# • `app.py` also has 2 print statements
#
# Total:
# • 1 from listes.py
# • 2 from app.py
#
# Fix:
# • Never put print statements at top level in modules
# • Use:
#
# if **name** == "**main**":
# # test code here
#
# • This prevents code from running when imported


shipping.cal_shipping_cost()