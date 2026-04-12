import re
string = "<HTML>Content</HTML>"
greedy = re.compile(r'.*')
not_greedy = re.compile(r'<.*?>')
answer1 = re.findall(greedy, string)
answer2 = re.findall(not_greedy, string)
print(answer1[0])
print(answer2[0])