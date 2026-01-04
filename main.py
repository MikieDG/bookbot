from stats import word_count, char_counter, sort_list
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...") 
    print("----------- Word Count ----------")
    print(f"Found {word_count(book)} total words") 
    print("--------- Character Count -------")
    sorted_chars = sort_list(char_counter(book))
    for item in sorted_chars:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    print("============= END ===============")
main()