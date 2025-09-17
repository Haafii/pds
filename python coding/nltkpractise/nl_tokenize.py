import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "Prof. Sasikala teaches Python."

tokens = word_tokenize(text)

print("Original Text:", text)
print("Tokenized Words:", tokens)
