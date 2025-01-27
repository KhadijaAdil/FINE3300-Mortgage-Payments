def mortgage_payments(principal, rate, amortization):
    #First, let's convert our percentage rate into a decimal
    rate_decimal = rate / 100

    #Next, let's calculate the appropriate rates for each period
    monthly_rate = ((1 + (rate_decimal)/2) ** (2/12)) -1
    semi_monthly_rate = ((1 + (rate_decimal)/2) ** (2/24)) -1
    bi_weekly_rate = ((1 + (rate_decimal)/2) ** (2/26)) -1
    weekly_rate = ((1 + (rate_decimal)/2) ** (2/52)) -1

    #Next, let's calculate the appropriate number of periods
    monthly_periods = amortization*12
    semi_monthly_periods = amortization*24
    bi_weekly_periods = amortization*26
    weekly_periods = amortization*52

    #Next, let's calculate the present value annuity factor for each period
    #Please note, pvaf stands for "present value annuity factor"
    monthly_pvaf = ((1 - (1 + monthly_rate) ** (-monthly_periods))) / monthly_rate
    semi_monthly_pvaf = ((1 - (1 + semi_monthly_rate) ** (-semi_monthly_periods))) / semi_monthly_rate
    bi_weekly_pvaf = ((1 - (1 + bi_weekly_rate) ** (-bi_weekly_periods))) / bi_weekly_rate
    weekly_pvaf = ((1 - (1 + weekly_rate) ** (-weekly_periods))) / weekly_rate

    #Next, let's calculate the periodic payments
    monthly_payment = principal / monthly_pvaf
    semi_monthly_payment = principal / semi_monthly_pvaf
    bi_weekly_payment = principal / bi_weekly_pvaf
    weekly_payment = principal / weekly_pvaf

    #Next, let's calculate the rapid payments
    rapid_bi_weekly_payment = monthly_payment / 2
    rapid_weekly_payment = monthly_payment / 4


    #Next, let's round to the nearest two decimal places
    monthly_payment = round(monthly_payment, 2)
    semi_monthly_payment = round(semi_monthly_payment, 2)
    bi_weekly_payment = round(bi_weekly_payment, 2)
    weekly_payment = round(weekly_payment, 2)
    rapid_bi_weekly_payment = round(rapid_bi_weekly_payment, 2)
    rapid_weekly_payment = round(rapid_weekly_payment, 2)

    #Finally, let's return all these values as a tuple
    return (monthly_payment, semi_monthly_payment, bi_weekly_payment, weekly_payment, rapid_bi_weekly_payment, rapid_weekly_payment)

#Let's get the inputs for the principal, rate, and amortization variables
principal_dollars = float(input("Enter the principal amount here (i.e. 100000): "))
rate_percentage = float(input("Enter the annual interest rate percentage here (i.e. 5.5): "))
amortization_years = float(input("Enter teh amortization period in years here (i.e. 25): "))

#Almost there - let's call the function now!
payments = mortgage_payments(principal_dollars, rate_percentage, amortization_years)

#Finally, it's time to print the values!
print(f"Monthly Payments: ${payments[0]:,.2f}")
print(f"Semi-Monthly Payments: ${payments[1]:,.2f}")
print(f"Bi-Weekly Payments: ${payments[2]:,.2f}")
print(f"Weekly Payment: ${payments[3]:,.2f}")
print(f"Rapid Bi-Weekly Payments: ${payments[4]:,.2f}")
print(f"Rapid Weekly Payments: ${payments[5]:,.2f}")

#Do I have to change the inputs so that they can be accepeted as $100,000 and 5.5%?