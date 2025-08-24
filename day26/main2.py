# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# numbers = [1, 2, 3]
# squares = [item * 2 for item in numbers]
# print(squares)

# [letter for letter in name]
# range_list = [number * 2 for number in range(1, 5)]
# print(range_list)


# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
#
# names_in_upper = [name.upper() for name in names if len(name) > 5]
#
# print(names_in_upper)


data1 = [3, 4, 6, 8, 9, 5, 7]
data2 = [13, 24, 6, 8, 10, 5, 8]

result = [number for number in data1 if number in data2]

print(result)

with open("file1.txt") as file:
    data1 = file.readlines()
    data1 = [int(number.strip()) for number in data1]

with open("file2.txt") as file2:
    data2 = file2.readlines()
    data2 = [int(number.strip()) for number in data2 ]

    result =[number for number in data1 if number in data2]

    print(result)
