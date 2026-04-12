import re
pattern = re.compile(r'\$\d+\.\d{2}')
message = "The total cost is $45.50 plus tax."
answers = re.findall(pattern,message)
print(answers)