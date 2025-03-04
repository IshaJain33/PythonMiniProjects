import random
import string

def generate_password(length=12):
    uppercase_letters = string.ascii_uppercase  
    lowercase_letters = string.ascii_lowercase  
    digits = string.digits                      
    special_chars = string.punctuation          
    all_characters = uppercase_letters + lowercase_letters + digits + special_chars
    password = (
        random.choice(uppercase_letters) +
        random.choice(lowercase_letters) +
        random.choice(digits) +
        random.choice(special_chars)
    )
    password += ''.join(random.choice(all_characters) for _ in range(length - 4))
    password = ''.join(random.sample(password, len(password)))

    return password

while True:
    try:
        length = int(input("Enter the desired password length (minimum 6): "))
        if length < 6:
            print("Password length should be at least 6 characters. Try again!")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a number.")

generated_password = generate_password(length)
print("\nGenerated Password:", generated_password)
