def main():
    sales_files = open("sales.txt", "r")


    for line in sales_files:
        amount = float(line)
        print(format(amount, ',.2f'))
    sales_files.close()


main()