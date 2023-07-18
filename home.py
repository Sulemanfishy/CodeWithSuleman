#TIP CALCULATOR APP
food_amount = float(input("Enter your food amount: "))
tip_percentage = float(input("Enter your tip percentage %: " )) / 100
tip_amount = food_amount * tip_percentage
print(tip_amount)
#total
total = food_amount + tip_amount
print(f"Tip amount :${tip_amount}")
print(f"Food amount :${food_amount}")
print(f"Total amount :${total}")
print ("$" + str(total))