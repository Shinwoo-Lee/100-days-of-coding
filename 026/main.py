import pandas

# TODO 1. Create a dictionary in this format:
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_string = input("Enter a word: ").upper()

result = [nato_dict[letter] for letter in input_string]
print(result)
