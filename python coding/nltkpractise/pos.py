import nltk
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
tokens = word_tokenize("Engineer designs wearable devices.")
print(nltk.pos_tag(tokens))