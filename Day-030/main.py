
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}













# import pandas as pd

# data = pd.read_csv("Day-026-Project/nato_phonetic_alphabet.csv")

# new_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# user_input = " "
# try:
#     suser_input = input("Pleas enter your name: ").upper()
# except:
#     print("Sorry this is not a word, please enter a word!")
#     while type(user_input) != " ":
#         user_input = input("Pleas enter your name: ").upper()
# else:
#     each_user_input_letter = [new_dict[letter] for letter in user_input]
# finally:
#     print("Hiiiiiii")
# print(each_user_input_letter)





# try:
#     file = open('text.txt')
# except:
#     print("this does not exist")

try:
    file = open('nothing.txt')
    lst = ['sdf', 'ghgg']
    dic = {'key': 'value'}
    # print(lst[2])
    print(dic["asdc"])
except FileNotFoundError:
    file.open("nothing.txt", 'w')
    file.write('Something')
except IndexError:
    print("This index does not exist")
except KeyError as error_message:
    print(f"this key {error_message} does not exist")
else:
    content = file.read()
    print(content)


# new_list = [new_item for item in list if test]
# compare each letter from then user input to see if code of that letter
# phoneric_list = [new_dict[letter] for letter in each_user_input_letter if letter in new_dict] 


