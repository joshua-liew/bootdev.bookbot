from stats import get_count_words, get_count_chars


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = get_count_words(text)
    print(F"{num_words} words found in the document")

    num_chars = get_count_chars(text)
    print(num_chars)


if __name__ == "__main__":
    main()
