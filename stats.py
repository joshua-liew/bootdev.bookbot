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
