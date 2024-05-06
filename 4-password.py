import random
import string

def generate_password(length, complexity):
    # Define character sets based on complexity
    if complexity == 'low':
        characters = string.ascii_lowercase + string.digits
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
        return None
    
    # Generate password using random.choices method
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    # Prompt user for password length
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid integer for the password length.")
        return
    
    # Prompt user for password complexity
    complexity = input("Enter the desired complexity level (low/medium/high): ").lower()
    
    # Check if password length is at least 6 characters
    if length < 6:
        print("Password length must be at least 6 characters.")
        return

    # Generate and display the password
    password = generate_password(length, complexity)
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
