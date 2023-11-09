# accept the total bill as input
total_bill = float(input("What is the total bill? "))
# accept the tip percentage as input
tip_percent = int(input("How many percent tip are you offering - 10, 12, or 15? "))
# finally, accept the number of people splitting the bill as input
num_of_people = int(input("How many people are splitting the bill? "))

# calculate the tip amount
tip_amount = tip_percent / 100  # divide the tip percent by 100
tip_amount *= total_bill  # multiply the tip amount with the total bill
total_bill += tip_amount  # add the tip amount to the total bill.

# calculate the amount each person will pay
# divide the total bill by the number of people paying
individual_bill = total_bill / num_of_people
print(f"Each person is paying: ${individual_bill:.2f}")
