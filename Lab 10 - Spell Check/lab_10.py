import re


# This function takes in a line of text and returns a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    """Runs the entire program"""
    dictionary = open("dictionary.txt")

    dictionary_list = []

    for line in dictionary:
        line = line.strip()
        dictionary_list.append(line)
    dictionary.close()

    print("--- Linear Search ---")

    alice = open("AliceInWonderLand200.txt")

    current_line = 0
    for line in alice:
        word_list = split_line(line)
        current_line += 1
        for word in word_list:
            key = word.upper()
            current_list_position = 0
            while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != key:
                current_list_position += 1
            if current_list_position == len(dictionary_list):
                print("Line", current_line, "possible misspelled word:", word)
    alice.close()

    print("--- Binary Search ---")

    dictionary = open("dictionary.txt")

    dictionary_list = []

    for line in dictionary:
        line = line.strip()
        dictionary_list.append(line)
    dictionary.close()

    alice = open("AliceInWonderLand200.txt")

    current_line = 0
    for line in alice:
        word_list = split_line(line)
        current_line += 1
        for word in word_list:
            key = word.upper()
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False

            while lower_bound <= upper_bound and not found:
                middle_pos = (lower_bound + upper_bound) // 2

                if dictionary_list[middle_pos] < key:
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > key:
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print("Line", current_line, "possible misspelled word:", word)
    alice.close()


main()
