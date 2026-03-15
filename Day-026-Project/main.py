
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas as pd

data = pd.read_csv("Day-026-Project/nato_phonetic_alphabet.csv")
# print(data.head)

new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(new_dict)

user_input = input("Pleas enter your name: ").upper()
print(user_input)

each_user_input_letter = [letter for letter in user_input]
print(each_user_input_letter)

new_list = [new_item for item in list if test]
# compare each letter from then user input to see if code of that letter
phoneric_list = [new_dict[letter] for letter in each_user_input_letter if letter in new_dict] 
print(phoneric_list)

# 'item_1':{
#         'places_to_buy': ['Publix', 'Costco', 'BJs', 'Aldi', 'Broward Meat', 'Walmart'],
#         'is_pack': 0, #should this be a function that ask how many packs 
#         'need_to_buy': True,
#         'frequency': 1; #if True add if by weekly
#     },

# grocery_list = {
#     'mulos':{
#         'places_to_buy': ['Costco'],
#         'is_pack': 0, #should this be a function that ask how many packs 
#         'need_to_buy': True
#     },
#     'eggs':{
#         'places_to_buy': ['Publix', 'Costco', 'Aldi', 'Walmart'],
#         'is_pack': 0, #should this be a function that ask how many packs 
#         'need_to_buy': True
#     },
#     'milk':{
#         'places_to_buy': ['Publix',],
#         'is_pack': 0, #should this be a function that ask how many packs 
#         'need_to_buy': False
#     },
# }




# grocery_list['Alitas']['places_to_buy'] = ['Costco']

# print(grocery_list)

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

