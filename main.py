def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    print(text)

    number_of_words = word_count(text)
    print(number_of_words)

    number_of_characters = character_count(text)
    print(number_of_characters)

def get_book_path(path):
    with open(path) as f:
        return f.read()

def word_count(passage):
    words = passage.split()
    return len(words)

def character_count(passage):
    characters = {}
    for c in passage:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

main()