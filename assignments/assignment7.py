import re

# Open file and read data
with open("input.txt", "r") as file:
    text = file.read()

# Find email patterns
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)

print("Email addresses found:")
for email in emails:
    print(email)
