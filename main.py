from stats import nb_words
from stats import get_occurence
from stats import get_sorted_list
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookname = sys.argv[1]
    book = get_book_text(bookname)
    occurences = get_occurence(book)
    words_count = nb_words(book)
    sorted_list = get_sorted_list(occurences)

    ### Printing the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookname}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_list :
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()