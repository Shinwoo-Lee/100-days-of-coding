#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# TODO 1: create list_of_names
with open("Input/Names/invited_names.txt") as name_data:
    list_of_names = name_data.read().split("\n")

# TODO 2: Write letter with list_of_names
with open("Input/Letters/starting_letter.txt") as letter_data:
    letter_contents = letter_data.read()
    for name in list_of_names:
        new_letter = letter_contents.replace("[name]", name)

        # TODO 3: Save the letter in the right directory
        with open(f"Output/ReadyToSend/Letter_for_{name}.txt", mode="x") as location:
            location.write(new_letter)

