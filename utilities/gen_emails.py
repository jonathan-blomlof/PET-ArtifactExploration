import sys
import random
import string

def generate_fake_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "aol.com", "icloud.com", "protonmail.com", "mail.com"]
    name_length = random.randint(5, 10)
    name = ''.join(random.choice(string.ascii_lowercase) for _ in range(name_length))
    domain = random.choice(domains)
    return f"{name}.{random.choice(string.ascii_lowercase)}@{domain}"

num_lines = 10000

if len(sys.argv) < 2:
    print("Usage: python script_name.py <file_name>")
    sys.exit(1)

file_name = sys.argv[1]
if len(sys.argv) >= 3:
    num_lines = int(sys.argv[2])

fake_emails = []
while len(fake_emails) < num_lines:
    fake_email = generate_fake_email()
    if fake_email in fake_emails:
        continue
    fake_emails.append(fake_email)

with open(file_name, "w") as file:
    for i, fake_email in enumerate(fake_emails):
        file.write(f"{i} {fake_email}\n")

print(f"Generated {num_lines} fake email addresses and saved them in '{file_name}'.")

