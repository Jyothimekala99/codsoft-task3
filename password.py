import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the character sets for the password
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digits_chars = string.digits
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    # Combine character sets based on complexity
    if length < 8:
        character_set = lowercase_chars + uppercase_chars + digits_chars
    else:
        character_set = lowercase_chars + uppercase_chars + digits_chars + special_chars

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

# Main program
if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired length of the password: "))
        if password_length <= 0:
            print("Invalid input. Password length must be a positive integer.")
        else:
            generated_password = generate_password(password_length)
            print("Generated Password: " + generated_password)
    except ValueError:
        print("Invalid input. Please enter a valid positive integer for password length.")
