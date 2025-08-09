from stats import get_count_words


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text("./books/frankenstein.txt")
    count = get_count_words(text)
    print(F"{count} words found in the document")


if __name__ == "__main__":
    main()
