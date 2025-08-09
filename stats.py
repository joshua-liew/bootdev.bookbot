def get_count_words(text):
    count = len(text.split())
    return count


def get_count_chars(text):
    res = {}
    for char in text.lower():
        if char not in res:
            res[char] = 0
        res[char] += 1
    return res


def print_report(word_count, char_count):
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in char_count:
        if d.get("char").isalpha():
            print(f"{d.get("char")}: {d.get("num")}")
    print("============= END ===============")


def to_sorted_list(d):
    res = []
    for key in d:
        tmp = {}
        tmp["char"] = key
        tmp["num"] = d[key]
        res.append(tmp)
    res.sort(reverse=True, key=sort_by_count)
    return res


def sort_by_count(item):
    return item["num"]
