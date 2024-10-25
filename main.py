def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    print(text)

    number_of_words = word_count(text)
    number_of_characters = character_count(text)

    chars_sorted_list = chars_dict_to_sorted_list(number_of_characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

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

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()