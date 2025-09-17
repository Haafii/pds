import nltk
from nltk.tokenize import word_tokenize

# Download required resources (only first time)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Sample text
text = "Prof. Sasikala teaches Python at Government Engineering College Idukki."

# Step 1: Tokenize
tokens = word_tokenize(text)

# Step 2: POS tagging
tagged = nltk.pos_tag(tokens)

# Step 3: Named Entity Recognition (NER)
entities = nltk.chunk.ne_chunk(tagged)

print("Named Entities:")
print(entities)
