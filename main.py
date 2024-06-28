def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_content(book_path)
    print(text)

def get_book_content(path):
    with open(path) as f:
        return f.read()
    

main()