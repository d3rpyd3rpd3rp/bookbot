def get_word_count(book_text):
    return len(book_text.split())

def get_character_count(book_text):
    book_text = book_text.lower()
    character_count = {}
    for character in book_text:
        if character not in character_count:
            character_count[character] = 0
        character_count[character] += 1
    return character_count