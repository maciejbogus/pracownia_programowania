import re

question = "To be, or not to be, that is the question."
words = re.findall("[a-zA-Z]{1,}",question)

print(f"{len(words)}")