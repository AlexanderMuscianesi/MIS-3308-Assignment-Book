import re
pattern = re.compile(r'[^\d\- ]')
message = "Contact: 555-1234!"
answers = re.findall(pattern,message)
print(answers)