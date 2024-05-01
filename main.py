def main(): 
    #Reach into Book Folder and Grab this text, used relative file path
    bookpath = "books/frankenstein.txt"
    #
    text=book_text_open(bookpath)
    word_total= word_count(text)
    lowercase_words=text_lowercase(text).split()
    letter_dict=letter_count(lowercase_words)
    print_count=sort_highest(letter_dict)
        
    print("--- Filepath: books/frankenstein.txt ---")
    print(f'{word_total} words found in the document')
    for item in print_count:
        print(f'The letter {item["Letter"]} was found {item["num"]} times')
    # print(f'{print_count}')
    print("--- Report End ---")

def sort_on(dict):
    return dict["num"]

def sort_highest(letter_dict):
    highest_count=[]
    for letter in letter_dict:
        highest_count.append({"Letter": letter, "num": letter_dict[letter]})
    highest_count.sort(reverse=True, key=sort_on)
    return highest_count

def letter_count(lowercase_words):
    text_dict={}
    #Loop over each word
    for word in lowercase_words:
        #Loop over each character in that space
        for character in word:
            #Check if the character is a letter "A or a" for ex
            #AND if it is NOT already in the dictionary. Set the key, and its value is 1
            if character.isalpha() and character not in text_dict:
                text_dict[character]=1
            #If the character is already in the key for the dict, increment 1
            elif character.isalpha() and character in text_dict:
                text_dict[character]+=1

    #Sort the dictionary keys
    sorted_dict=sorted(text_dict)
    #initialize new dictionary to set keys, then take values from our dict
    #those values will be assigned to the keys in alphabetical order
    final_dict={}
    for letter in sorted_dict:
        final_dict[letter]=text_dict[letter]
    return final_dict


def word_count(text):
    words=text.split()
    return len(words)

def text_lowercase(text):
    lowercase=text.lower()
    return lowercase

def book_text_open(bookpath):
    with open(bookpath) as f:
        file_contents = f.read()
        return file_contents
main()