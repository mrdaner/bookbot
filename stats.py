def get_num_words(text):
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