import logging

logging.basicConfig(filename='logs.log', 
                    format='%(asctime)s::%(levelname)s::%(message)s::', 
                    level=logging.INFO)

def predict_loan(income, married, age):
    """Given the income, marital status and age of a person this function will predict the loan amount"""

    if (type(income) not in [int, float]):
        logging.error('Income is not of type Float')        
        raise TypeError("Income is not of type Float")
    elif (type(married) not in [ bool]):
        logging.error('Married is not type Int or Bool')
        raise TypeError('Married is not of type Int or Bool')
    elif (type(age) not in [int, float]):
        logging.error('Age is not of type of Int')
        raise TypeError('Age is not of type of Int')
    elif (income < 600000):
	    logging.error('Income is less than 600000')
	    raise ValueError('Income is less than 600000')
    elif (age < 18) or (age > 60):
        logging.error('Age is not in between 18 and 60')
        raise ValueError('Age is not in between 18 and 60')
    else:
        loan_amount = 50000 + 0.5 * (income) - 0.1 * (married) - 0.05 * (age)
        logging.info('For income :{}, married : {}, age :{} the loan amount : {}'.format(income, married, age, loan_amount))
        return round(loan_amount, 3)

def predict(i, m, a):
    try:
        out = str(predict_loan(i, m, a))
    except TypeError:
        out = "TypeError"
    except ValueError:
        out = "ValueError"
    finally:
        return out

if __name__ == "__main__":
    print("Loan amount: ", predict(650000.00, True, 22))
    print("Loan amount: ", predict(650000.00, False, 22))
    print("Loan amount: ", predict(750000.00, True, 22))

    print("Loan amount: ", predict(500000.00, True, 22))
    print("Loan amount: ", predict(650000.00, False, 16))

    print("Loan amount: ", predict(650000.00, -1, 22))
    print("Loan amount: ", predict(750000.00, 2, 22))
    print("Loan amount: ", predict("Salary", True, 2+3j))
