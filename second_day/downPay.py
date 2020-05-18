house_price = 1000000
good_credit = True
if good_credit:
    down = house_price*.1
else:
    down = house_price*.2
print(f"Your downpayment for this house is ${down}")