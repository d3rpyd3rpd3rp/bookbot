def get_word_count(book_text):
    return len(book_text.split())

def get_character_count(book_text):
    book_text = book_text.lower()
    character_count = {}
    for char in book_text:
        if char not in character_count:
            character_count[char] = 0
        character_count[char] += 1
    return character_count

def sort_on(items):
    return items["num"]

def get_sorted_dictionary(character_count):
    chars = []
    for k, v in character_count.items():
        if not k.isalpha():
            continue
        chars.append({"char" : k, "num" : v})
    chars.sort(reverse=True, key=sort_on)
    return chars