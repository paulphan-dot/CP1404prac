# 1. Ask the user for their name, then write it to name.txt, using open/close for this question.
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2. Read the name from name.txt and print a greeting, using open/close for this question
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3. Read the first two numbers from numbers.txt and print the results, use with for this question
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    result = first_number + second_number
print(result)

# 4. Print the total for all lines in numbers.txt using with for this question
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)
