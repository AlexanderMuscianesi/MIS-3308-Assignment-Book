import re
string = "Orders: 5 apples, 12 oranges, 99 bananas"
inventory = re.compile(r'\d+\s\w+')
answers = re.findall(inventory, string)
print(answers)