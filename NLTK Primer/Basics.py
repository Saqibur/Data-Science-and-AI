from __future__ import division
import nltk, re, pprint

fileobj = open("DotaChat.txt", 'r', encoding='utf-8')
raw_chat_text = fileobj.readlines()

chat_str = ""

for line in raw_chat_text:
    chat_str += line.replace("\n", " ")

tokens = nltk.word_tokenize(chat_str)
nltk_text = nltk.Text(tokens)
print('; '.join(nltk_text.collocation_list())) # need this, otherwise error, too many values to unpack.