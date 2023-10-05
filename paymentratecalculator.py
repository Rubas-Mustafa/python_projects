# collect the necassary inputs: principal(loan amount), apr, years
# calculate the monthly payment
# show to the user
def main():
    
    principal = float(input("Input the loan amount:  "))
    apr = float(input("Input the interest rate:  "))
    years = int(input("Amount of Years: "))

    monthly_rate = apr/1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** (-amount_of_months))

    print("%2f" % monthly_payment)

main()