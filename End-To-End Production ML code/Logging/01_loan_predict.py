import math 

def predict_loan(income, married, age):
    """Given the income, marital status and age of a person this function will predict the loan amount"""

    if ((type(income) in [int, float]) and
        (type(married) in [bool]) and
        (type(age) in [int, float]) and
        (income >= 600000) and 
        ((age >= 18) or (age <= 60))):
        return (50000 + 0.5 * (income) - 0.1 * (married) - 0.05 * (age))
    else:
        return 0


if __name__ == "__main__":
    print("Loan amount: ", predict_loan(650000.00, True, 22))
    print("Loan amount: ", predict_loan(550000.00, False, 18))

