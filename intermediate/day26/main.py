import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
nato_alphabet = {row.letter:row.code for (index, row) in data.iterrows()}
# print(result)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
nato = (nato_alphabet[letter] for letter in word)
print(nato)
