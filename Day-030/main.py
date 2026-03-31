
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}





import pandas as pd

data = pd.read_csv("Day-026-Project/nato_phonetic_alphabet.csv")
# print(data.head)


new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(new_dict)

def error_handler():
    user_input = input("Pleas enter your name: ").upper()
    try: 
        each_user_input_letter = [new_dict[letter] for letter in user_input]
    except KeyError as error_message:
        print(f"enter only letter this {error_message} is not a STRING")
        error_handler()
    else:
        return each_user_input_letter

# new_list = [new_item for item in list if test]
# compare each letter from then user input to see if code of that letter
phoneric = error_handler()
print(phoneric)







# try:
#     file = open('text.txt')
# except:
#     print("this does not exist")

# try:
#     file = open('some_file.txt')
#     d = {'key': 'value'}
#     print(d['key'])
# except FileNotFoundError:
#     file = open('some_file.txt', 'w')
#     file.write("Hello World")
# except KeyError as error_message:
#     print(f'This {error_message}, is not a key')
# else:
#     content = file.read()
#     print(content)





