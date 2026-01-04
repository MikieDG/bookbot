def word_count(book):
    words = book.split()
    return len(words)

def char_counter(book):
    char_count = {}
    for char in book:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    return char_count

def sort_on(item):
    return item["num"]

def sort_list(chars):
    sorted_list = []
    for char in chars:
        num = chars[char]
        char_dict = {"char": char, "num": num}
        sorted_list.append(char_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list