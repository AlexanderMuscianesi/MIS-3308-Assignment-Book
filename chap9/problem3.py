import re
pattern = re.compile(r'colou?r')
message = "Americans say color, Brits say colour. I can't tell the difference."
checks = re.findall(pattern,message)
print(checks)