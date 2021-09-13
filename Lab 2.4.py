 #Student ID:1201201282
 #Student Name:Tay Xi Yang 



banana = 1.50
grape = 5.60
print("Invoice for Fruits Purchase")
print("------------------------------")
quantity1 = int(input("Enter the quantity (comb) of bananas bought: "))
quantity2 = int(input("Enter the amount (kg) of grapes bought: "))
total1 = quantity1 * banana
total2= quantity2 * grape
total_price = total1 + total2
print("Item             Qty      Price       Total")
print("Banana (combs)   {:.0f}    RM{:.2f}    RM{:.2f}".format(quantity1, banana, total1))
print("Grapes (kg)      {:.0f}    RM{:.2f}    RM{:.2f}".format(quantity2, grape, total2))
print("Total: RM{:.2f}".format(total_price))