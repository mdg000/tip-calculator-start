# 100 Days of Code Practice Project
# Tip Calculator Program

print("Welcome to the tip calculator\n")
amount = float(input("What was the total bill? $"))
percent = float(input("What percentage tip would you like to give? 10, 12, or 15\n"))
people = int(input("How many people to split the bill?\n"))
tipamount = percent / 100
owed = ((amount * tipamount) + amount) / people
final = "{:.2f}".format(owed)

print(f"Each person should pay: ${final}")
