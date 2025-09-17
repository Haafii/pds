import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Downloading required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Sample book titles
data = {'title': [
    "Introduction to Thermodynamics for Mechanical Engineers",
    "Data Structures and Algorithms in Python",
    "Digital Electronics and Microprocessor Design",
    "Fluid Mechanics Fundamentals",
    "Operating System Concepts",
    "Analog Electronics and Circuits",
    "Machine Design and Manufacturing",
    "Artificial Intelligence with Python",
    "Control Systems Engineering",
    "Computer Networks and Security"
]}
df = pd.DataFrame(data)

# NLTK preprocessing functions
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def preprocess_title(title):
    # Tokenize
    tokens = word_tokenize(title.lower())
    # Remove stopwords and non-alphabetic tokens
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    # Lemmatization
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    return lemmatized_tokens

# Keyword sets for classification
mech_keywords = {'thermodynamics', 'fluid', 'mechanics', 'machine', 'manufacturing', 'design', 'control', 'engineering'}
cse_keywords = {'data', 'algorithm', 'operating', 'system', 'artificial', 'intelligence', 'computer', 'network', 'security', 'python'}
ece_keywords = {'electronics', 'digital', 'microprocessor', 'analog', 'circuit'}

def classify_title(title):
    tokens = preprocess_title(title)
    # Check keywords intersection
    if any(word in mech_keywords for word in tokens):
        return 'Mechanical (Mech)'
    elif any(word in cse_keywords for word in tokens):
        return 'Computer Science (CSE)'
    elif any(word in ece_keywords for word in tokens):
        return 'Electronics (ECE)'
    else:
        return 'Unclassified'

# Apply classification
df['category'] = df['title'].apply(classify_title)

print(df)
