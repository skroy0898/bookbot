from collections import defaultdict


def main():
    book_path = "books/frankenstein.txt"
    contents = get_book_text(book_path)
    num_words = word_count(contents)
    letter_count = count_letters(contents)
    letter_list = dict_to_list(letter_count)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in letter_list:
        if not item["letter"].isalpha():
            continue
        print(f"The '{item['letter']}' character was found {item['num']} times")

    print("--- End report ---")

def get_book_text(path: str) -> str:
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def word_count(contents: str) -> int:
    words = contents.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_letters(contents: str) -> dict:
    contents = contents.lower()
    letter_map = defaultdict(int)

    for letter in contents:
        if ord(letter) >= 97 and ord(letter) <= 127:
            letter_map[letter] = 1 + letter_map.get(letter, 0)
    
    return letter_map

def sort_on(d: dict):
    return d["num"]

def dict_to_list(letter_count: dict) -> list:
    sorted_list = []
    
    for letter in letter_count:
        sorted_list.append({"letter": letter, "num": letter_count[letter]})
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()