#TODO 1. Create a dictionary in this format:

# {"A": "Alfa", "B": "Bravo"}




#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
import pandas as pd
nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {value.letter : value.code for (index,value) in nato_df.iterrows()}
print(nato_dict)

answer = input("Enter the name").upper().replace(" ","")
answer_nato = [nato_dict[value] for value in answer]
print(answer_nato)