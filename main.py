book = "books/frankenstein.txt"
with open(book) as f:
    file_contents = f.read()

# count_words counts number of words in text
def count_words(text):
    count = len(text.split())
    return count

# counts number of each character
def count_char(text):
    char_dict = {}
    low_text = text.lower()
    for i in range(0, len(low_text)):
        if low_text[i] in char_dict:
            char_dict[low_text[i]] += 1
        else:
            char_dict[low_text[i]] = 1
    
    count_char_lst = list(char_dict.items()) # transform dictionary in a list
    count_char_lst.sort()

    # counts only character from alphabet
    alpha_count = [] 
    for item in count_char_lst:
        if item[0].isalpha():
            alpha_count.append(item)

    alpha_count.sort(key=lambda alpha_count: alpha_count[1], reverse=True) # sort decending by number
    
    return alpha_count

# Prints report
def prnt_report(book, words, char_count):
    print("")
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document")
    print("")

    for item in char_count:
        print(f"The '{item[0]}' character was found {item[1]} times")

    print("--- End report ---")



prnt_report(book, count_words(file_contents), count_char(file_contents))
