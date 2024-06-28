def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_content(book_path)
    words = get_number_words(text)
    characters = get_char_appear(text)
    sorted_list = sort_list(characters)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print()

    for item in sorted_list:
        print(f"The '{item["character"]}' character was found {item["occurence"]} times")
    
    print("--- End report ---")

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

def sort_on(dict):
    return dict["occurence"]

def sort_list(characters):
    sorted_list = []
    for character in characters:
        if character.isalpha():
            sorted_list.append({"character": character, "occurence": characters[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    

main()