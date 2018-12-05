import string 
import sys

d = {}
total_of_word = 0

with open("english_words.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

def is_english(word):
    return word.lower() in english_words

def uncipher(plaintext, shift):
    plaintext = plaintext.lower()
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    output = plaintext.translate(table)
    is_english_word = 0
    for index, word in enumerate(output.split(), start=1):
        if is_english(word):
            is_english_word+=1
        d['output_'+str(shift)] = {'text': output, 'is_english_word': is_english_word }
        total_of_word = index
    return d


def wrap_dict():
    for shift in range(1, 27):
        uncipher("rkzzi mrbscdwkc dy ofobiyxo", shift)

    for dict in d:
        if d[dict]['is_english_word'] > 0 :
            print(d[dict]['text'])


wrap_dict()



