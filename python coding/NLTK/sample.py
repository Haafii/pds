import nltk

# Download required resources
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')

# Sample text
text = """Professor visited Chennai, then flew to New York
for a conference.
He also stopped by Paris and Tokyo before returning to
India."""

# 1. Sentence Tokenization
sentences = nltk.sent_tokenize(text)

# 2. Word Tokenization
tokenized_sentences = [nltk.word_tokenize(sent) for sent in sentences]

# 3. PoS Tagging
tagged_sentences = [nltk.pos_tag(sent) for sent in tokenized_sentences]

# 4. Named Entity Chunking
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False)

# 5. Extract location entities
def extract_places(tree):
    places = []
    for subtree in tree:
        if hasattr(subtree, 'label') and subtree.label() in ('GPE', 'LOCATION'):
            place = " ".join([leaf[0] for leaf in subtree.leaves()])
            places.append(place)
    return places

# 6. Collect all places
all_places = []
for tree in chunked_sentences:
    all_places.extend(extract_places(tree))

print("Identified Places:", set(all_places))
