# 1 to 100 units - 1.5Rs
# 101 to 200 units - 2.5Rs
# 201 to 300 units - 4Rs
# 300 to 350 units - 5Rs
# Above 350 - Fixed charge 1500Rs

def ElectricityBillCal(units):
    if units >  0 and units < 100:
        payment = units * 1.5
        fixedcharge = 25
    elif units > 100 and units < 200:
         payment = (100 * 1.5) + (units - 100) * 2.5
         fixedcharge = 50
    elif units > 200 and units < 300:
        payment = (100 * 1.5) + ( 200 - 100) * 2.5 + ( units - 200) * 4
        fixedcharge = 75
    elif units > 300 and units < 350:
        payment = (100 * 1.5) + (200 - 100) * 2.5 + (300 - 200) * 4 + (units - 300) * 5
        fixedcharge = 100
    else:
        payment = 0
        fixedcharge = 1500

    return payment + fixedcharge

units = float(input("Enter the Units that you Consumed: "))
TotalBill = ElectricityBillCal(units)

print(f'Total Bill is: {TotalBill:.2f}')

    