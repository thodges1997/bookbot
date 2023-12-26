def main():
    book = get_book_text("books/franky.txt")
    words = get_num_words(book)
    print(words)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()