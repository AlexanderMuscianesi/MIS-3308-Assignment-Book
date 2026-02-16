#Problem 2) Checkout Receipt Builder 
import sys
# -- INPUTS --
item_name = " "
item_count = 0
subtotal = 0 
while item_name != "Done":
    print("Enter your item or type Done")
    item_name = str(input())
    if item_name == str("Done"):
        print("Okay, Exiting")
        break
    item_count = item_count + 1
    print("Enter Price")
    price = float(input())
    print("Enter Quantity")
    quantity = int(input())
    print("Your Subtotal is:")
    subtotal = price * quantity + subtotal
    print("$",subtotal)
# -- VALIDATION -- 
    if price <= float(0):
        print("Invalid Price")
        sys.exit()
    if quantity < 1:
        print("Invalid Quantity")
        sys.exit()
# -- RULES -- 
if subtotal >= 100 :
    discount = float(0.1)
else: 
    discount = 0
tax = float(0.07)
# -- CALCULATIONS -- 
taxed_total = subtotal - (subtotal*discount)
final_total = taxed_total + (taxed_total*tax)
print("Outputting Results")
print("Item Count:",item_count)
print("Subtotal: $",subtotal)
print("Discount: ",discount)
print("Taxed Total: $",taxed_total)
print("Final Total: $",final_total)
print("End Problem 2")