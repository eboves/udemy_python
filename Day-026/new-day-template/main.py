"""
Day 26 - [Project Name]
100 Days of Code - Python
Angela Yu's Python Bootcamp

Description:
[NATO: A way to communicate around the world using a set of rules around the world. ]

Author: [Your Name]
Date: [3/13/26]
Course: Udemy - 100 Days of Code: The Complete Python Pro Bootcamp
"""

# List Comprehension 
num = [1,2,3,4]
# new_list = [new_item for item in list]
new_list = [n + 1 for n in num]
# print(new_list)

name = "Elvis"
name_list = [letter for letter in name]
# print(name_list)

new_range_list = [n * 2 for n in range(1,5)]
# print(new_range_list)

names = ['Elvis', 'Karen', 'no', "ni", 'Jef']
new_name_list = [nam for nam in names if len(nam) < 4]
print(new_name_list)
# n = "elvis"
# print(len(n))





