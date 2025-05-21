from stats import count_words, character_count, sort_dict
import sys

def get_book_text(book):
    with open(book, encoding='utf-8') as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        return num_words

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    total_words = get_book_text(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    unique_chars = character_count(book)
    print("--------- Character Count -------")

    for dict in sort_dict(unique_chars):
        if dict["char"].isalpha() == True:
            print(f"{dict['char']}: {dict['num']}")

main()