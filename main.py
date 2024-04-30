def main(): 
    bookpath = "books/frankenstein.txt"
    text=book_text_open(bookpath)
    word_total= word_count(text)
    lowercase_words=text_lowercase(text).split()
    letter_dict=letter_count(lowercase_words)
    # lowercase_words_flattend=lowercase_words.concat()
    print(f'{word_total} words found in the document')
    # print(f'Lowercase {lowercase_words}')
    print(f'{letter_dict}')

def letter_count(lowercase_words):
    total_text_array=[]
    for word in lowercase_words:
        for character in word:
            total_text_array.append(character)
    print(total_text_array)
    # print(items(total_text_array))


def book_text_open(bookpath):
    with open(bookpath) as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    words=text.split()
    return len(words)

def text_lowercase(text):
    lowercase=text.lower()
    return lowercase

main()