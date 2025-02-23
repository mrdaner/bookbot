from stats import *

def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        print(f"--- Begin report of {path} ---")
        print(f"{get_num_words(file_contents)} words found in the document")

        char_counts = count_characters(file_contents)
        for char_data in char_counts:
            print(f"The '{char_data["char"]}' character was found {char_data["num"]} times")

        print(f"--- End report ---")
main()