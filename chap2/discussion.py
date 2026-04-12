subtotal = 0
import sys
order_number = str(input("Please enter order number:"))
subtotal = float(input("Please enter the subtotal of customer's purchase."))

if subtotal <= 0:
    print("Invalid Amount")
    sys.exit()
tax_rate = float(.06625)
tax = subtotal*tax_rate
total = tax + subtotal
print("Subtotal with Tax, $",total)
tip = float(input("Tip received? $"))
if tip = 0:
    print ("Front of House Order, No Tip")
else :
    print ("Enjoy mopping up later tonight!")
final_total = tip + total
print("Final Total: $",final_total)