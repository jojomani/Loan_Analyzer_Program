#### Loan Analyzer Program ####

import csv
from pathlib import Path

"""Part 1: Automate the Calculations. Automate the calculations for the loan portfolio summaries.
"""
loan_costs = [500, 600, 200, 1000, 450]

# Number of loans that are in the list.
number_of_loans = len(loan_costs)
print(f"The total number of loans in the list is {number_of_loans}")

# Total of all loans in the list. 
loans_total = sum(loan_costs)
print(f"The total of all loans is {loans_total}")

# Average price of the loan.
loans_average = loans_total / number_of_loans
print(f"The average loan price is ${loans_average}")


"""Part 2: Analyze Loan Data.
"""

# Loan data
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Future value and remaining months
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"The future value of the loan is ${future_value}")
print(f"The remaining months are {remaining_months}")


# Calculating present value
discount_rate = 0.20
present_value = future_value / (1+discount_rate/12) ** remaining_months
print(f"The present value of the loan is ${round(present_value, 2)}")

# If-else statement to determine worthiness of the loan cost. 

if present_value >= loan.get("loan_price"):
    print(f"The loan is worth at least the cost to buy it")
else:
    print(f"The loan is too expensive and not worth the price")


"""Part 3: Perform Financial Calculations.
"""

# Defining a new function that will be used to calculate present value.

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

annual_discount_rate = 0.2
def pv(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1+annual_discount_rate/12) ** remaining_months
    return present_value

present_value = pv(new_loan.get("future_value"), new_loan.get("remaining_months"), annual_discount_rate)
print(f"The present value of the loan is ${round(present_value, 2)}")


"""Part 4: Conditionally filter lists of loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Creating empty lists for `inexpensive_loans` and 'expensive_loans'
inexpensive_loans = []
expensive_loans = []

# Looping through all the loans and append any that cost $500 or less to the `inexpensive_loans` list and above $500 to the 'expensive_loans' list

for loan_price in loans:
    if loan_price["loan_price"] <= int(500):
        inexpensive_loans.append(loan_price)
    elif loan_price["loan_price"] > int(500):
        expensive_loans.append(loan_price)

print(f"These loans are expensive {expensive_loans}")
print(f"Here is the list of inexpensive loans {inexpensive_loans}")


"""Part 5: Save the results.
"""

# Setting the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Setting the output file path
csvpath = Path("src/inexpensive_loans.csv")

# Using the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.

print("Writing the inexpensive loans data to a CSV file for the business analysts team...")

with open(csvpath, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)

    for row in inexpensive_loans:
        csvwriter.writerow(row.values())

#####                                                #####
##### Extra - Writing a CSV file for expensive loans #####

# Setting the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Setting the output file path
csvpath = Path("src/expensives_loans.csv")

# Using the csv library and `csv.writer` to write the header row 
# and each row of `loan.values()` from the `expensive_loans` list.

print("Writing the expensive loans data to a CSV file for the business analysts team...")

with open(csvpath, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)

    for row in expensive_loans:
        csvwriter.writerow(row.values())

############################################################
############### End of Loan Analyzer Program ###############
