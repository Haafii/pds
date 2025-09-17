import requests
from bs4 import BeautifulSoup
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.corpus import stopwords

# Download required NLTK data (only run once)
nltk.download("punkt")

nltk.download("maxent_ne_chunker")
nltk.download("words")
nltk.download("stopwords")

nltk.download("averaged_perceptron_tagger_eng")

# Target URL
url = "https://www.thehindu.com/"
keyword = "Latest News"

# Send GET request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract all visible text
text_blocks = soup.find_all(["p", "li", "h1", "h2", "h3", "div", "a"])

print(f"Searching for '{keyword}' on {url}")
found = False
all_text = ""

for block in text_blocks:
    text = block.get_text(strip=True)
    if keyword.lower() in text.lower():
        print(f"🔍 Found '{keyword}':")
        print(text)
        print("-" * 60)
        found = True
    all_text += text + " "

if not found:
    print(f"Keyword '{keyword}' not found in the extracted text blocks.")

# -----------------------------
# NLTK Named Entity Recognition
# -----------------------------
tokens = word_tokenize(all_text)
tokens = [t for t in tokens if t.lower() not in stopwords.words("english")]

tagged = pos_tag(tokens)
chunks = ne_chunk(tagged)

names = []
locations = []

for chunk in chunks:
    if hasattr(chunk, "label"):
        if chunk.label() == "PERSON":
            names.append(" ".join(c[0] for c in chunk))
        elif chunk.label() == "GPE":  # Geo-Political Entity (cities, countries, states)
            locations.append(" ".join(c[0] for c in chunk))

# Remove duplicates
names = list(set(names))
locations = list(set(locations))

print("\n📰 Extracted Entities from News:")
print("People Mentioned:", names)
print("Cities/Countries Mentioned:", locations)
