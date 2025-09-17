import spacy

import nltkpractise.ner_spacy as ner_spacy

# Load English NLP model
nlp = ner_spacy.load("en_core_web_sm")

# Input text
text = """Prof. Sasikala visited Chennai, then flew to New
York for a conference.
She also stopped by Paris and Tokyo before returning to
India."""

# Process text
doc = nlp(text)

# Extract places (GPE = geopolitical entities, LOC = locations)
places = [ent.text for ent in doc.ents if ent.label_ in ("GPE", "LOC")]

# Print results
print("Identified Places:", set(places))
