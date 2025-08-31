import re

text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

# Raw strings
print(r"\tTab")

# re.compile: build regex pattern object
# matching phone numbers
pattern = re.compile(r"[89]00[-.]\d\d\d[-.]\d\d\d\d")

# re.findter: create iters of Match objects
matches = pattern.finditer(text_to_search)
print("Matching phone numbers")
print(f"Pattern: {pattern.pattern}\n")
for match in matches:
    print(match)
print("*" * 90)

# matching with ranges
pattern = re.compile(r"[a-zA-z]")  # match letters
matches = pattern.finditer(text_to_search)
print("Matching with ranges")
print(f"Pattern: {pattern.pattern}\n")
for match in matches:
    print(match)
print("*" * 90)

# matching with ^ (not)
pattern = re.compile(r"[^a-zA-z]")
matches = pattern.finditer(text_to_search)
print("Matching with ^(not)")
print(f"Pattern: {pattern.pattern}\n")
for match in matches:
    print(match)
print("*" * 90)

# matching with quantifiers
pattern = re.compile(r"\d{3}[.-]\d{3}[.-]\d{4}")
matches = pattern.finditer(text_to_search)
print("Matching with quantifiers")
print(f"Pattern: {pattern.pattern}\n")
for match in matches:
    print(match)

pattern = re.compile(r"Mr\.?\s[A-Z]\w*")
print(f"Pattern: {pattern.pattern}\n")
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
print("*" * 90)

# matching with groups
pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*")
matches = pattern.finditer(text_to_search)
print("Matching with groups")
print(f"Pattern: {pattern.pattern}\n")

for match in matches:
    print(match)
print("*" * 90)

# Grouppings
urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
matches = pattern.finditer(urls)
print("Grouppings example")
print(f"Pattern: {pattern.pattern}\n")
for match in matches:
    print(match.group(3))  # 0: entire match; 1: first group

# re.sub: substitution with groups
subbed_urls = pattern.sub(r"\2\3", urls)
print(subbed_urls)
print("*" * 90)
# Matching emails
emails = """
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
"""

pattern = re.compile(r"[a-zA-Z0-9.-]+@[a-zA-Z.-]+\.(com|edu|net)")

matches = pattern.finditer(emails)

for match in matches:
    print(match)

# Searching in a file
with open("Python/Built-in Modules/re/data.txt", "r") as f:
    contents = f.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print(match)

"""
re methods
"""

# re.findall: return all non-overlapping matches of pattern in string, as a list of strings or tuples
pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*")
matches = pattern.findall(text_to_search)
print("re.findall examples")
print(f"Pattern: {pattern.pattern}\n")

for match in matches:
    print(match)
print("*" * 90)

# re.match: if the beginning of string match the regex, return a corresponding Match object.
sentence = "Start a sentence and then bring it to an end"
pattern = re.compile(r"Start")
matches = pattern.match(sentence)
print(matches)

# re.search: return the first Match
pattern = re.compile(r"sentence")
matches = pattern.search(sentence)
print(matches)

# Flags
pattern = re.compile(r"start")  # I for ignorecase
matches = pattern.search(sentence)
print(matches)
