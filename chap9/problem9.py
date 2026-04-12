import re
pattern = re.compile(r'^Hello.*Goodbye$')
message1 = "Hello Friend Goodbye"
message2 = "Friend Hello"
message3 = "Hi Hello Goodbye"
answers1 = re.findall(pattern, message1)
print (answers1)
answers2 = re.findall(pattern, message2)
print (answers2)
answers3 = re.findall(pattern, message3)
print (answers3)