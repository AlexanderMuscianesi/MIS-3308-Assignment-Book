import re
bottles = re.compile(r'Bottles+')
message = "oh yeah man I love Bottles I love when I have a Bottle with me woah man Bottlessssss"
answers = re.findall(bottles, message)
print(answers)