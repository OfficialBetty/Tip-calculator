#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total_bill = 150.00
print("Welcome to the tip caculator!")
input("what was the total bill? $")
input("How much tip would you like to give? 10, 12, or 15? ")
input("How many people are spliting the bill? ")

tip = 12 / 100 
bill = float(124.56) *  tip
a_float = bill
limited_float = round(a_float, 2)
#print(limited_float)
bill = limited_float
#print(bill)
total_bill = 124.56 + bill
#print(total_bill)
each_person = total_bill / 7
result = each_person
print(f"each person should pay: ${result}")


 


