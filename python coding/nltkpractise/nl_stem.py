import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem("teaching"))
print(stemmer.stem("studies"))