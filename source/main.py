##
# discord_messages_as_emojis.py
# Date: 08/05/2023
# Author: Ryan Gordon
# Converts a string of text to regional indicator emojis for discord

def ask_yes_no_question(prompt):
    """Asks a yes or no question and returns the answer as True or False."""
    answer = ""
    while answer not in ("y", "yes", "n", "no"):
        answer = input(prompt).strip().lower()
        if answer not in ("y", "yes", "n", "no"):
            print("Please enter either yes or no.")
    return answer in ("y", "yes")


def convert(string):
    """
    Converts a string of text to regional indicator emojis for discord.

    param string (str): The string of text to convert.

    return (str): The string that will be converted to regional indicators
        by discord.
    """
    output, processing_emoji = "", False

    for char_index in range(0, len(string)):
        character = string[char_index]

        if character == ":":
            processing_emoji = not processing_emoji

        if processing_emoji and ":" in string[char_index:]:
            output += character
            continue

        if character.lower() in ALPHABET:
            output += f":regional_indicator_{character.lower()}:"
        elif character in NUMBERS.keys():
            output += NUMBERS[character]
        elif character == " ":
            output += ":blue_square:"
        else:
            output = output.strip() + character
            continue

        output += " "

    return output


ALPHABET = set("abcdefghijklmnopqrstuvwxyz")

NUMBERS = {
    "0": ":zero:",
    "1": ":one:",
    "2": ":two:",
    "3": ":three:",
    "4": ":four:",
    "5": ":five:",
    "6": ":six:",
    "7": ":seven:",
    "8": ":eight:",
    "9": ":nine:"
}

if __name__ == "__main__":
    # Loop until the user doesn't want to convert any more strings
    keep_converting = True
    while keep_converting:
        string_to_convert = input("Enter the string to convert: ")
        print(convert(string_to_convert))
        keep_converting = ask_yes_no_question("Convert another string? ")
