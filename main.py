def main():
    book = get_book_text("books/franky.txt")
    words = get_num_words(book)
    chars = char_counter(book)
    final_report = report(book)
    print(final_report)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def char_counter(text):
    char_table = {}
    words = text.split()
    for word in words:
        for char in word:
            lowered = char.lower()
            if lowered in char_table:
                char_table[lowered] += 1
            else:
                char_table[lowered] = 1
    return(char_table)

def report(text):
    char_table = char_counter(text)
    num_words = get_num_words(text)
    char_list = list(char_table.keys())
    char_list.sort()

    ret_string = f"---- Begin Report of Frankenstein Characters ---- \n {num_words} words found in the text \n"

    for char in char_list:
        if char.isalpha() and char == "z":
            ret_string = ret_string + f"The character {char} was found {char_table[char]} times \n ---- End of Report ----"
        elif char.isalpha():
            ret_string = ret_string + f"The character {char} was found {char_table[char]} times \n"
        
    return ret_string

main()