import re
pattern = re.compile(r'\b[A-Z]\w*[aeiou]\w*\d\b')
string = "Apple1 Apple2 3Apple 4pple Apple5 apple6 aPPLE7"
answers = re.findall(pattern, string)
print (answers)