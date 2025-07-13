from stats import *
import sys

def get_content(book):
     with open(book) as f:
        file_contents = f.read()
        return file_contents

def main():
    # book_path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        content = get_content(book_path)
        num_words = get_word_count(content)
        chars_dict = get_character_count(content)
        chars_sorted = sort_dictionaries (chars_dict)
        get_character_count (book_path)
        print ("============ BOOKBOT ============")
        print (f"Analyzing book found at {book_path}")
        print ("----------- Word Count ----------")
        print (f"Found {num_words} total words")
        print ("--------- Character Count -------")
        for character in chars_sorted:
            print (character["char"] + ": " + str(character["count"]))
        print ("============= END ===============")

main()