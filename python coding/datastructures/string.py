# ----------------------------------------
# String Operations Practice Toolkit
# ----------------------------------------

def q1_count_vowels():
    word = "engineering"
    vowels = "aeiouAEIOU"
    count = sum(1 for ch in word if ch in vowels)
    print("Q1: Number of vowels:", count)


def q2_replace_word():
    text = "good morning"
    new_text = text.replace("morning", "evening")
    print("Q2:", new_text)


def q3_check_substring():
    sentence = "wearable device for safety"
    print("Q3:", "safe" in sentence)


def q4_find_index():
    sentence = "programming for data science"
    index = sentence.lower().find("data")
    print("Q4: Starting index:", index)


def q5_join_words():
    words = ["machine", "learning", "project"]
    dash_str = "-".join(words)
    print("Q5:", dash_str)


def q6_clean_spaces():
    sentence = "   Python programming    is fun   "
    cleaned = " ".join(sentence.split())
    print("Q6:", cleaned)


def q7_check_numeric():
    pin = "682021"
    print("Q7:", pin.isdigit())


def q8_check_alphanumeric():
    pan = "ABCDE1234F"
    print("Q8:", pan.isalnum())


# -------------------------------
# Run All or Menu Driven
# -------------------------------
def run_all():
    q1_count_vowels()
    q2_replace_word()
    q3_check_substring()
    q4_find_index()
    q5_join_words()
    q6_clean_spaces()
    q7_check_numeric()
    q8_check_alphanumeric()


if __name__ == "__main__":
    print("=== String Operations Practice ===")
    print("1. Run All")
    print("2. Run Individual Question")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        run_all()
    else:
        while True:
            print("\nSelect Question (1-8) or 0 to Exit:")
            q = input("Enter number: ")
            if q == "0":
                break
            elif q == "1": q1_count_vowels()
            elif q == "2": q2_replace_word()
            elif q == "3": q3_check_substring()
            elif q == "4": q4_find_index()
            elif q == "5": q5_join_words()
            elif q == "6": q6_clean_spaces()
            elif q == "7": q7_check_numeric()
            elif q == "8": q8_check_alphanumeric()
            else:
                print("Invalid choice. Try again.")
s = " Hello, World! 123\n"

# --- Case Conversion ---
print(s.lower())       # lowercase
print(s.upper())       # uppercase
print(s.title())       # title case
print(s.capitalize())  # only first letter
print(s.swapcase())    # swap case
print(s.casefold())    # aggressive lowercase

# --- Search & Replace ---
print(s.find("World"))         # index of substring
print(s.rfind("l"))            # last occurrence
print(s.index("World"))        # index (error if not found)
print(s.replace("World", "Earth"))
print(s.count("l"))            # count occurrences

# --- Splitting & Joining ---
print(s.split())               # split on whitespace
print(s.rsplit(",", 1))        # split from right
print(s.splitlines())          # split lines
print(",".join(["a", "b"]))    # join list

# --- Trimming & Padding ---
print(s.strip())               # remove whitespace
print(s.lstrip())              # remove left spaces
print(s.rstrip())              # remove right spaces
print("cat".center(7, "*"))    # center pad
print("cat".ljust(6, "-"))     # left pad
print("cat".rjust(6, "-"))     # right pad
print("42".zfill(5))           # zero fill

# --- Validation Methods ---
print(s.isalnum())             # alphanumeric?
print("Hello".isalpha())       # all alphabets?
print("123".isdigit())         # all digits?
print("12.3".isdecimal())      # decimal?
print("42".isnumeric())        # numeric?
print(" \n".isspace())         # whitespace?
print("ABC".isupper())         # uppercase?
print("abc".islower())         # lowercase?
print("Hello World".istitle()) # title case?
print("foo_bar".isidentifier())# valid identifier?
print("abc".isascii())         # ASCII?
print("abc!".isprintable())    # printable?

# --- Formatting ---
print("Hello, {}".format("Alice"))
print("{name} is {age}".format_map({"name": "Bob", "age": 30}))
name = "Eve"
print(f"Hello, {name}")

# --- Translation ---
trans_table = str.maketrans("HW", "hw")
print("Hello World".translate(trans_table))

# --- Partition & Slicing ---
print("abc:123:def".partition(":"))
print("abc:123:def".rpartition(":"))
print("abcdef"[2:5])
