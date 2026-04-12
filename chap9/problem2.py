import re
group_phone_reg = re.compile(r'(\d{3})-(\d{3}-\d{4})')
msg = "My number is 415-555-4242"
msgreg= group_phone_reg.search(msg)
area_code, main_number = msgreg.groups()
print(f"Area Code: ({area_code})")
print(f"Main Number: {main_number}")