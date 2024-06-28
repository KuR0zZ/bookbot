def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_content(book_path)
    words = get_number_words(text)

def get_book_content(path):
    with open(path) as f:
        return f.read()

def get_number_words(text):
    words = text.split()
    return len(words)
    

main()