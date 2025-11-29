import sys

if len(sys.argv) < 4:
    print("Usage: python Billing_receipt.py <item name> <quantity> <price per unit> <discount>")
    sys.exit(1)

item_name = sys.argv[1]
quantity = int(sys.argv[2])
price = float(sys.argv[3])

# If discount not given, set it to 0
discount = float(sys.argv[4]) if len(sys.argv) >= 5 else 0

total = quantity * price
final_amount = total - discount

print("Item:", item_name)
print("Quantity:", quantity)
print("Price per Unit:", price)
print("Discount:", discount)
print("Total Amount:", final_amount)
