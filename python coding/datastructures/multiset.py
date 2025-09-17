# Install: pip install multiset
from multiset import Multiset

# 1. Create a multiset from a list with duplicates
print("\n--- Example 1: Multiset Creation ---")
ms = Multiset(['apple', 'banana', 'apple', 'orange', 'banana', 'banana'])
print("Multiset:", ms)


# 2. Perform union, intersection, difference, and addition on two multisets
print("\n--- Example 2: Set Operations ---")
set1 = Multiset([1, 2, 2, 3])
set2 = Multiset([2, 2, 2, 3, 4, 4])
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Addition:", set1 + set2)


# 3. Find symmetric difference of multiple sets
print("\n--- Example 3: Symmetric Difference ---")
test_list = [
    {5, 3, 2, 6, 1},
    {7, 5, 3, 8, 2},
    {9, 3},
    {0, 3, 6, 7}
]
sym_diff = set()
for s in test_list:
    sym_diff ^= s
print("Symmetric difference:", sym_diff)


# 4. Print the minimum and maximum of a set
print("\n--- Example 4: Min and Max ---")
A = {5, 3, 8, 2, 9}
print("Minimum:", min(A))
print("Maximum:", max(A))


# 5. Find common symptoms among patients
print("\n--- Example 5: Common Symptoms ---")
patients_symptoms = [
    Multiset(["fever", "cough", "headache"]),
    Multiset(["fever", "cough", "sore throat"]),
    Multiset(["fever", "headache", "cough"]),
]
common_symptoms = patients_symptoms[0]
for symptoms in patients_symptoms[1:]:
    common_symptoms &= symptoms
print("Common symptoms across patients:", common_symptoms)


# 6. Simple query classification using multiset
print("\n--- Example 6: Query Classification ---")
categories = [
    ("sports", Multiset(["football", "basketball", "tennis", "game", "player"])),
    ("technology", Multiset(["computer", "software", "internet", "programming", "code"])),
    ("travel", Multiset(["vacation", "flight", "hotel", "destination", "trip"])),
]

def classify_query(query, categories):
    query_multiset = Multiset(query.lower().split())
    best_score, best_match = 0, None
    for name, keywords in categories:
        score = len(query_multiset & keywords)
        if score > best_score:
            best_score, best_match = score, name
    return best_match

query = "Going by flight for the football match"
print("Predicted category:", classify_query(query, categories))


# 7. Medical diagnosis using multiset for symptoms
print("\n--- Example 7: Medical Diagnosis ---")
def diagnose(symptoms, conditions):
    potential_diagnoses = []
    for condition_name, condition_symptoms in conditions:
        if symptoms.issubset(condition_symptoms):
            print(f"Condition: {condition_name}")
            print(f"Symptoms: {condition_symptoms}")
            potential_diagnoses.append(condition_name)
    return potential_diagnoses

conditions = [
    ("Allergies", Multiset(["runny nose", "sore throat", "cough", "sneezing", "itchy eyes", "congestion"])),
    ("Influenza", Multiset(["fever", "cough", "muscle aches", "headache", "fatigue"])),
    ("Common Cold", Multiset(["runny nose", "sore throat", "fever", "cough", "headache"])),
]

patient_symptoms = Multiset(["runny nose", "sore throat", "cough"])
potential_diagnoses = diagnose(patient_symptoms, conditions)

if potential_diagnoses:
    print("Potential diagnoses:")
    for diagnosis in potential_diagnoses:
        print("-", diagnosis)
else:
    print("No matching conditions found.")
