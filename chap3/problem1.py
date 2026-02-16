#Problem 1) Sales Commission Calculator
import sys
# -- INPUTS --
sales_amount = float(input("Sales Amount ($): "))
region = str(input("E/W/C : "))
# -- VALIDATION --
if sales_amount <= float(0):
    print("Invalid Sales Amount, Try Again.")
    sys.exit()
if region != str("E") and region != str("W") and region != str("C") :
    print("Incorrect Region, Try Again.")
    sys.exit()
# -- RULES --
if sales_amount < float(1000):
    rate= float(0.02)
if sales_amount >= float(1000) and sales_amount <= float(4999.99):
    rate= float(0.04)
if sales_amount >= float(5000):
    rate= float(0.06)
if region == str("E"):
    bonus = (50)
if region == str("W"):
    bonus = (25)
if region == str("C"):
    bonus = (0)
# -- CALCULATIONS --
base_commission = rate * sales_amount
final_commission = base_commission + bonus 
# -- OUTPUT --
print("Outputting Results")
print("Sales Amount: $",sales_amount)
print("Region:",region)
print("Rate:",rate)
print("Base Commission: $",base_commission)
print("Final Commission: $",final_commission)
print("End Problem 1")


