# Task 1. Make a program that has some sentence (a string) on input and returns a
# # dict containing all unique words as keys and the number of occurrences as values.
# Define function for deleting punctuation from string.


def del_punctuation(string):
    if ',' in string:
        string = string.replace(',', '')
    if '.' in string:
        string = string.replace('.', '')
    if ';' in string:
        string = string.replace(';', '')
    if ':' in string:
        string = string.replace(':', '')
    if '?' in string:
        string = string.replace('?', '')
    if '!' in string:
        string = string.replace('!', '')
    return string


text = input('Write, please, any sentence for future dictionary: ')

text = del_punctuation(text)
lst_word = text.split()
dict_word = {}
for word in lst_word:
    dict_value = lst_word.count(word)
    dict_word[word] = dict_value

# Creation the dict using comprehension.
dict_word2 = {word: lst_word.count(word) for word in lst_word}

print(dict_word)
print(dict_word2)