# Opens the file so the python code can read it. 
log_file = open("um-server-01.txt") 


# Declare a function called sales_reports with a parameter of log_file
def sales_reports(log_file): 
    # Take the argument passed through log_file and loops through every line.
    # The data passed through each iteration is represented by the line variable.
    for line in log_file: 
        # Take the line and removes any trailing whitespace characters
        line = line.rstrip()
        # Each character in the line is given an index. In this case the first 3 characters represent the day of week.
        # Take the first 3 indexes (the end index is excluded) and assign them to a variable called day
        day = line[0:3]
        # Create a condition that checks the value of day for each line.
        if day == "Mon":
            # Print the line where the condition is true (beginning of line starts with Mon)
            print(line)

# Invoke the function that was just created and pass throught the opened document as the argument.
sales_reports(log_file)

# Extra credit
log_file.seek(0)

def melon_orders(log_file):
    for line in log_file:
        lineSplit = line.strip().split(' ')
        if int(lineSplit[2]) > 10:
            print(line)

melon_orders(log_file)