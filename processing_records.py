import os # Need to remove and rename functions
def main():
    # Create a bool variable to use as a flag
    found = False
    # Get the coffee to delete
    search = input("Which employee do you want to delete? ")
    # Open the original coffee.txt file
    emp_file = open("employees.txt", "r")
    temp_file = open("temp.txt", "w")
    # Read the first records description field
    name = emp_file.readline()

    while name != '' :
        qty = float(emp_file.readline())
        # Strip the \n from the description
        name = name.rstrip("\n")
        if name != search:
            # Write the record to the temp file
            temp_file.write(name + "\n")
            temp_file.write(str(qty) + "\n")
        else:
            # Set the found flag to True
            found = True
        # Read the next description
        name = emp_file.readline()
        # Close the coffee file and the temporary file
        emp_file.close()
        temp_file.close()
        # Delete the original emp file
        os.remove("employees.txt")
        # Rename the original file
        os.rename("temp.txt", "employees.txt")
        # If the search value was not found in the file
        # Display a message
        if found:
            print("The file has been updated.")
        else:
            print("That item was not found in the file.")

main()
