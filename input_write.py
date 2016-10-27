def main():
    print("Enter the name of three friends: ")
    name1 = input("Friend #1: ")
    name2 = input("Friend #2: ")
    name3 = input("friend #3: ")


    my_file = open("philosophers.txt", "w")


    my_file.write(name1 + '\n')
    my_file.write(name2 + '\n')
    my_file.write(name3 + '\n')


    my_file.close()
    print("The names were written to friends.txt.")


main()