# Date: 1/21/2020
# Subject: List
nums = [6, 1, 45, 9, 55]
# print(len(takes))
# takes = list(range(1, 4))
# print(len(takes))
# for num in nums:
#     print(num)

# index = 0
# while index < len(nums):
#     print(f"{index} is : {nums[index]}")
#     index += 1

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
result = ''
for sound in sounds:
    result += sound.upper()

print(result)
# Class completed: 103

# Date: 02/04/2020
# Class : 104  
# learning the append or extend to add elements in the lust
# 'Insert'--> add an element in a given position 
# ends at class 106

# Date: 2/14/2020
# ends at class 110

# Date: 2/17/2020
# !begin at class 111 List Comprehension

numbers = [1, 2, 3, 4, 5]
double_numbers = []

for num in numbers:
    double_number = num * 2
    double_numbers.append(double_number)
print(double_numbers)

numbers = [12, 13, 14, 15, 16]
doubleNumbers = [num * 2 for num in numbers]
print(doubleNumbers)

name = 'colt'
newName = [char.upper() for char in name]
print(newName)

friends = ['ashley', 'matt', 'michael']
friendName = [friend[1].capitalize() for friend in friends]
print(friendName)

# Date: 2/23/2020
# Class ends at 112, List Comprehension with logic
numbers = [1, 2, 3, 4, 5, 6]
result = [num * 2 if num % 2 == 0 else num / 2 for num in numbers]
print(result)


# Date: 2/24/2020
# Nested list
# Complete List Class 
# Go for Dictionary Class 121

nestedList = [[1, 2, 3],[4, 5,6], [7,8,9]]
for l in nestedList:
    for value in l:
        print(value)

# Test the Git cloone again
