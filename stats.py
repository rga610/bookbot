# text = "Hello, world!"


# Takes the book and counts the number of words
def count_words(text):
    words = text.split()
    words = len(words)
    return words


# Takes the text from the book as a string, and returns the number of times each character appears
def count_chars(words):
    words = words.lower()
    chars = {}
    for char in words:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars


def sort_on(items):
    return items["count"]


def sorted_list(text):
    chars = count_chars(text)
    chars_list = []
    for char, count in chars.items():
        chars_list.append({"char": char, "count": count})

    chars_list.sort(reverse=True, key=sort_on)

    for char in chars_list:
        print(f"{char['char']}: {char['count']}")
    return chars_list
