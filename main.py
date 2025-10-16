import random, string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    print("Generated password:", generate_password())
