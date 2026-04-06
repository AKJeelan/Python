is_high_income = True
is_good_credit = False
eligible_for_loan = False
is_criminal_record = True

if is_high_income and is_good_credit:
    eligible_for_loan = True
elif not is_criminal_record:
    eligible_for_loan = True

if eligible_for_loan:
    print("Eligible for loan")
else:
    print("Not eligible")