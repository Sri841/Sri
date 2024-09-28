import random
import string

def generate_password(length, use_digits, use_special_chars):
    characters = string.ascii_letters 
    
    if use_digits:
        characters += string.digits 

    if use_special_chars:
        characters += string.punctuation  

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the length of the password: "))
        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        if length < 1:
            print("Password length should be at least 1.")
        else:
            password = generate_password(length, use_digits, use_special_chars)
            print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a number for the length.")

if __name__ == "__main__":
    main()
