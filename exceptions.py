def main():
    # Get two numbers
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    # If num2 is not 0, divide num1 by num2
    # and display the result
    if num2 != 0:
        result = num1 / num2
        print(num1, "divided by", num2, "is", result)
    else:
        print("Cannot divide by zero.")


main()


def main():
    try:
        hours = int(input("How many hours did you work? \n"))
        pay_rate = float(input("Enter your hourly pay rate: "))
        gross_pay = hours * pay_rate
        print("Gross pay: ", format(gross_pay, ',.2f'), sep='')
    except ValueError:
        print("ERROR: Hours worked and hourly pay rate must")
        print("be valid integers")
    except ValueError as err:
        print(err)


main()
