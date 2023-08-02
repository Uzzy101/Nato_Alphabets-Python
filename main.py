import pandas

aplh_csv = pandas.read_csv('nato_phonetic_alphabet.csv')
alph_df = pandas.DataFrame(aplh_csv)


#Loop through rows of a data frame
nato_alph_dict = {row.letter: row.code for (index, row) in alph_df.iterrows()}


#Create a list of the phonetic code words from a word that the user inputs.

word = input('Write any word: ').upper()
code_list = [nato_alph_dict[letter] for letter in word]
print(code_list)

