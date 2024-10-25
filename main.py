def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    print(text)

def get_book_path(path):
    with open(path) as f:
        return f.read()

main()