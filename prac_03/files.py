DATA_FILENAME = "data.txt"
NUMBER_FILENAME = "number.txt"
TOTAL_NUMBER = 0
out_file = open(DATA_FILENAME, "w")

# Read File

name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# Read File

in_file = open(DATA_FILENAME, "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

in_file = open(NUMBER_FILENAME, "r")
first_number = int(in_file.readline())
second_number = int(in_file.readline())
in_file.close()
print(f"Sum of first two numbers is: ", first_number + second_number)


in_file = open(NUMBER_FILENAME, "r")
for line in in_file:
    number = int(line)
    TOTAL_NUMBER += number

in_file.close()
print("Total number is: ", TOTAL_NUMBER)
