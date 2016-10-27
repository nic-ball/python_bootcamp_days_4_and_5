def main():
    sales = open("sales.txt.txt", "r")
    line = sales.reading()


    while line != "":
        amount = float(line)
        print(format(amount, ",.2f"))
        line = sales.readline()

    sales.close()


main()