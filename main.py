def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    print(text)

    number_of_words = word_count(text)
    print(number_of_words)

def get_book_path(path):
    with open(path) as f:
        return f.read()

def word_count(passage):
    words = passage.split()
    return len(words)

main()