from stats import get_count_words, get_count_chars, to_sorted_list, print_report


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = get_count_words(text)
    num_chars = get_count_chars(text)
    num_chars_list = to_sorted_list(num_chars)
    print_report(num_words, num_chars_list)


if __name__ == "__main__":
    main()
