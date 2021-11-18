import re
question = "To be, or not to be, that is the question"
lowercase = re.findall("[aeiouy]{1}", question)

print(len(lowercase))