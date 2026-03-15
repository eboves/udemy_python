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

""" 02 Pandas Data Frame Dictionary List comprehension """
# existing_dict = {keys: values}
# df = pd.DataFrame(existing_dict)
# new_df = {key: value for (index, row) in df.iterrows()} #this is how to iterate through the rows in a pandas df.




""" 01 Dictionary List comprehension """
# new_dict = {new_key: new_value for item in dict.items() if test}
import random

names = ['Elvis', 'Karen', 'no', "ni", 'Jef']
new_dict = {person:random.randint(1, 100) for person in names}
# print(new_dict)

above_60 = {n:v for n,v in dict.items(new_dict) if v > 60}
# print(above_60)





""" 00 List comprehension """
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
# print(new_name_list)
# n = "elvis"
# print(len(n))

num = [2,5,3,7] 
new_num_list = [n * 3 for n in num if n > 4]
# print(new_num_list)




