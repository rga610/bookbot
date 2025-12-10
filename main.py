import sys
from stats import count_words, count_chars, sorted_list

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)

file_path = sys.argv[1]

# Loads and reads the book
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


# Main function
def main():
    text = get_book_text(file_path)
    words = count_words(text)

    print(
        f"============ BOOKBOT ============\nAnalyzing book found at {file_path}...\n----------- Word Count ----------\nFound {words} total words\n--------- Character Count -------"
    )
    sorted_list(text)
    print("============= END ==============")


if __name__ == "__main__":
    main()
