#import nltk
import re
import string
# load text
filename = "julioverne.txt"
file = open(filename, 'rt',encoding='utf-8-sig')
text = file.read()
file.close()

words = text.split()

print("*****First 100 words*****\n")
print(words[:100])

words = re.split(r'\W+',text)
print("*****Words without puctuation with re*****\n")
print(words[:200])

print(string.punctuation)

re_punc = re.compile('[%s]' % re.escape(string.punctuation))

stripped = [re_punc.sub("",w) for w in words]

print("\n*****Stripped words*****\n")                   
print(stripped[:200])

#----------------------------------------------#

"""
método string.lower() -> convertir a minúsculas una cadena
se le aplica a cadenas de texto (se tiene que aplicar antes de que se separen las palabras)
"""

text_lower = text.lower()
words_lower = text_lower.split()

print("*****First 100 words LOWERED*****\n")
print(words_lower[:100])