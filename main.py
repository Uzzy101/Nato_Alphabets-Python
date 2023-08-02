# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98],
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# with open('nato_phonetic_alphabet.csv') as uzzy:
#     data = uzzy.read()
#     print(data)

import pandas
#student_data_frame = pandas.DataFrame(student_dict)
aplh_csv = pandas.read_csv('nato_phonetic_alphabet.csv')
alph_df = pandas.DataFrame(aplh_csv)


#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
nato_alph_dict = {row.letter: row.code for (index, row) in alph_df.iterrows()}
#print(nato_alph_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input('Write any word: ').upper()
code_list = [nato_alph_dict[letter] for letter in word]
print(code_list)

