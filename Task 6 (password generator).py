import random
import string

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    charset = ''
    if use_upper:
        charset += string.ascii_uppercase
    if use_lower:
        charset += string.ascii_lowercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += "!@#$%^&*()-_=+[]{};:,.<>?/"

    return ''.join(random.choice(charset) for _ in range(length))

# Password categories
passwords = {
    "Easy": generate_password(8, use_upper=False, use_symbols=False),  # Only lowercase + digits
    "Medium": generate_password(8, use_symbols=True),                  # Short but mixed chars
    "Okay": generate_password(12, use_symbols=True),                   # 12 chars mixed
    "Strong": generate_password(14, use_symbols=True),                 # Long, mixed, high entropy
    "Very Strong": generate_password(18, use_symbols=True)              # Very long, mixed
}

# Output results
for level, pwd in passwords.items():
    print(f"{level} Password: {pwd}")
