from stats import get_book_text, get_num_words, get_number_of_times_character_appear, get_sorted_list_of_dictionaries
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    word_count = get_num_words(book_text)
    sorted_list_of_dictionaries = get_sorted_list_of_dictionaries(get_number_of_times_character_appear(book_text))
    print(f"""============ BOOKBOT ============
            Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    for dict in sorted_list_of_dictionaries:
        if dict["name"].isalpha():
           print(f"{dict["name"]}: {dict["num"]}") 
        continue

main()