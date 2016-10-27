def main():
    num_days = int(input("For how many days do " + "you have sales?\n"))
    sales_file = open("sales", "w")


    for count in range(1, num_days + 1):
        sales = float(input("Enter the sales for day " + str(count) + ": \n"))

        sales_file.write(str(sales) + "\n")


    sales_file.close()
    print("Date written to sales.txt\n")

main()

def main():
    sales = open("sales", "r")
    line = sales.readline()


    while line != "":
        amount = float(line)
        print(format(amount, ",.2f"))
        line = sales.readline()


    sales.close()


main()

