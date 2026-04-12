import re
phone_number_regex = re.compile(r'\d{3}-\d{4}')
message = "The code is 888-1234"
phone_number = phone_number_regex.search(message)
print(f"The code is : {phone_number.group()}")