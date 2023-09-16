with open("file1.txt") as file_1:
    first_file = file_1.readlines()
    # print(first_file)
with open("file2.txt") as file_2:
    second_file = file_2.readlines()
    # print(second_file)
result = [int(number) for number in first_file if number in second_file]

print(result)
