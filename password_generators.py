import random
import string

def generate_password(length, uppercase=True, lowercase=True, numbers=True, special_chars=True):
    characters = ""
    
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type should be allowed.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Strong Password Generator!")

    try:
        length = int(input("Enter the desired password length: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    numbers = input("Include numbers? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    if not (uppercase or lowercase or numbers or special_chars):
        print("At least one character type should be allowed.")
        return

    print("\nGenerating passwords:")
    for _ in range(num_passwords):
        password = generate_password(length, uppercase, lowercase, numbers, special_chars)
        print(password)

    print("\nPasswords generated successfully!")

if __name__ == "__main__":
    main()
