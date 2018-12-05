import string 
import sys
import argparse

d = {}
total_of_word = 0

parser = argparse.ArgumentParser(description='Process some caesar code')
parser.add_argument('caesar', metavar='caesar', type=str, help='Put some caesar code')
parser.add_argument('--dict', dest='path_dict', nargs='?',default=False, help='Dict of your language')

args = parser.parse_args()
args = vars(parser.parse_args())

if args['path_dict']:
    file = args['path_dict']
else :
    file = "english_words.txt"

with open(file) as word_file:
    dict_words = set(word.strip().lower() for word in word_file)

def search_words(word):
    return word.lower() in dict_words

def uncipher(plaintext, shift):
    plaintext = plaintext.lower()
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    output = plaintext.translate(table)
    is_word = 0
    for index, word in enumerate(output.split(), start=1):
        if search_words(word):
            is_word+=1
        d['output_'+str(shift)] = {'text': output, 'is_word': is_word }
        total_of_word = index
    return d


def wrap_dict():
    for shift in range(1, 27):
        uncipher(args['caesar'], shift)

    for dict in d:
        if d[dict]['is_word'] > 0 :
            print(d[dict]['text'])


wrap_dict()



