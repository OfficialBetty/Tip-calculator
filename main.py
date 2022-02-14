#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪


# Write your code below this line 👇

print("Welcome to the tip caculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are spliting the bill? " ))

tip_as_percent = tip / 100 
total_tip_amount = bill * tip_as_percent
the_total_tip_amount = round(total_tip_amount, 2)
the_total_tip_amount = "{:.2f}".format(total_tip_amount)

total_bill = bill + total_tip_amount
the_total_bill = round(total_bill, 2)
the_total_bill = "{:.2f}".format(total_bill)

bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Total bill is: ${the_total_bill}\nThe tip amount is: ${the_total_tip_amount}\nThe bill per person is: ${final_amount}")


 


