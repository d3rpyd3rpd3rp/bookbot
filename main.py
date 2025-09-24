from stats import *

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    print(f"Found {word_count} total words")
    print(f"{character_count}")

main()