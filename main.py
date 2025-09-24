def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_word_count(book_text):
    return len(book_text.split())

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_word_count(book_text)
    print(f"Found {num_words} total words")

main()