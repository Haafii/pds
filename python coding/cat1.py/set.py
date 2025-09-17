# Student data
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88,
    "Eva": 95,
    "Frank": 60,
    "Grace": 70,
    "Hannah": 82,
    "Ian": 90,
    "Jack": 65
}

skills = {
    "Alice": {"Python", "ML"},
    "Bob": {"Python", "SQL"},
    "Charlie": {"C++", "DSA"},
    "David": {"Python", "AI"},
    "Eva": {"ML", "AI"},
    "Frank": {"C", "SQL"},
    "Grace": {"Python", "C++"},
    "Hannah": {"ML", "DataViz"},
    "Ian": {"AI", "SQL"},
    "Jack": {"C++", "Python"}
}

late_submissions = {"Charlie", "Frank", "Jack"}

# 1. Sort and print top 3 performers
top3 = sorted(students.items(), key=lambda x: x[1], reverse=True)[:3]
print("Top 3 Performers:", top3)

# 2. Highlight students who submitted late
print("Late submissions:", late_submissions)

# 3. Store each student’s (name, score) as tuple
tuples = [(name, score) for name, score in students.items()]
print("Tuples (name, score):", tuples)

# 4. Use dictionary to map student to (score, skills, late status)
details = {
    name: (students[name], skills[name], name in late_submissions)
    for name in students
}
print("Details dictionary:")
for k, v in details.items():
    print(k, ":", v)

# 5. Common and unique skills
all_skills = list(skills.values())
common_skills = set.intersection(*all_skills)
unique_skills = set.union(*all_skills)
print("Common skills:", common_skills)
print("All unique skills:", unique_skills)

# 6. Store skill summary as tuple
skill_summary = [(name, tuple(skills[name])) for name in students]
print("Skill Summary:", skill_summary)
