def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        print(count_words(file_contents))
        print(count_characters(file_contents))

def count_words(text):
    return len(text.split())

def count_characters(text):
    character_dictionary = {}
    text = text.lower()
    character_set = set(text)
    for unique_character in character_set:
        character_dictionary[unique_character] = text.count(unique_character)
    return character_dictionary
    

main()