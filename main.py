def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_content(book_path)
    words = get_number_words(text)
    characters = get_char_appear(text)

def get_book_content(path):
    with open(path) as f:
        return f.read()

def get_number_words(text):
    words = text.split()
    return len(words)

def get_char_appear(text):
    character = {}
    lowercase_string = text.lower()
    for char in lowercase_string:
        if char in character:
            character[char] += 1
        else:
            character[char] = 1
    return character
    

main()