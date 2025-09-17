import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('omw-1.4')

syns = wordnet.synsets("teach")
print(syns[0].definition())
