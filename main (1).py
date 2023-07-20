#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator")
bill=input("what was the total bill $")
tip=input("How much tip youu want to give? 10,12 or 15 ")
People=input("how many people you want to split you bill")
people=int(People)
bill=float(bill)
tip=int(tip)
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"final amount {final_amount}")





#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇