#TODO: Create a letter using starting_letter.txt
stripnames = []
with open("./input/Letters/starting_letter.txt",mode="r") as template:
    temp = template.read()

with open("./input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()
    for name in names:
        stripnames.append(name.strip())

print(stripnames)

for name in stripnames:
    new_letter = temp.replace("[Name]", name)

    filename = f"letter_for_{name}.txt"
    with open(filename, "w") as file:
        file.write(new_letter)





#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp