def get_word_count(book):
    with open(book) as f:
        file_contents = f.read()
        words= file_contents.split()
        word_count = len(words)
        print (f"{word_count} words found in the document")