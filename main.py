from stats import *
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    book_text = get_book_text(sys.argv[1])
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_dictionary = get_sorted_dictionary(character_count)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------\nFound {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_dictionary:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()