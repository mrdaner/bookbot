def count_words(text):
    return len(text.split())

def sort_on(dictionary):
    return dictionary["num"]

def count_characters(text):
    chars_d = {}
    text = text.lower()
    character_set = set(text)
    for unique_character in character_set:
        if unique_character.isalpha():
            chars_d[unique_character] = text.count(unique_character)
    
    chars_l = []
    for char, count in chars_d.items():
        chars_l.append({"char": char, "num": count})

    chars_l.sort(reverse=True, key=sort_on)
    return chars_l

def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        print(f"--- Begin report of {path} ---")
        print(f"{count_words(file_contents)} words found in the document")

        char_counts = count_characters(file_contents)
        for char_data in char_counts:
            print(f"The '{char_data["char"]}' character was found {char_data["num"]} times")

        print(f"--- End report ---")
main()