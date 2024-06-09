import random
import string

def generate_password(length):
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lower + upper + digits + symbols

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt user for password length
        length = int(input("Enter the desired length of the password: "))
        
        # Ensure the length is a positive integer
        if length <= 0:
            print("Please enter a positive integer for the password length.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Generated password: {password}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the password generator
main()
