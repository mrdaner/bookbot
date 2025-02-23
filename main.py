import sys
from stats import *

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    path = sys.argv[1]
    
    with open(path) as f:
        file_contents = f.read()
        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print(f"----------- Word Count ----------")
        print(f"Found {get_num_words(file_contents)} total words")
        print(f"--------- Character Count -------")
        char_counts = count_characters(file_contents)
        for char_data in char_counts:
            print(f"{char_data["char"]}: {char_data["num"]}")

        print(f"============= END ===============")

main()