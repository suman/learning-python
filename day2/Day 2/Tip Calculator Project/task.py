print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_in_amount = bill * tip / 100
total_bill_amount = round((( tip_in_amount + bill) / 5), 2)
print(f"Total amount for each member is {total_bill_amount}")