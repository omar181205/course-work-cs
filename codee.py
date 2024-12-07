import random  # Import the random module for generating random numbers

def is_prime(n):  # Function to check if a number is prime
    if n <= 1:  # Numbers <= 1 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisors up to the square root of n
        if n % i == 0:  # If divisible, n is not prime
            return False
    return True  # If no divisors, n is prime

def generate_prime():  # Function to generate a random prime number
    while True:  # Keep trying until we find a prime
        num = random.randint(2, 100000)  # Generate a random number in the range
        if is_prime(num):  # Check if the number is prime
            return num  # Return the prime number

def is_primitive_root(g, p):  # Function to check if g is a primitive root modulo p
    required_set = {num for num in range(1, p)}  # All integers from 1 to p-1
    actual_set = {pow(g, exp, p) for exp in range(1, p)}  # Compute g^exp % p for all exp
    return required_set == actual_set  # g is a primitive root if both sets match

def generate_primitive_root(p):  # Function to find a primitive root modulo p
    for g in range(2, p):  # Test integers starting from 2
        if is_primitive_root(g, p):  # Check if g is a primitive root
            return g  # Return the first primitive root found

def key_generation():  # Function to generate cryptographic keys
    global p, g, a, e  # Declare variables as global to use them across functions
    p = generate_prime()  # Generate a random prime number
    print(f"Random prime number (p): {p}")  # Display the prime number
    g = generate_primitive_root(p)  # Find a primitive root modulo p
    print(f"Random primitive root modulo {p} (g): {g}")  # Display the primitive root
    a = random.randint(1, p - 2)  # Select a random private key a
    e = pow(g, a, p)  # Compute the public key e = g^a % p
    print(f"Receiver's Key: ( p={p},g={g}, e={e})")  # Display the keys

def encryption():  # Function to encrypt a message
    global c1, c2  # Declare variables for the ciphertext
    if 'p' not in globals() or 'g' not in globals() or 'e' not in globals():  # Check if keys are generated
        print("Key generation must be performed first.")  # Warn if keys are missing
        return

    m = int(input(f"Enter the message to encrypt (m, as an integer less than {p}): "))  # Input message
    if m >= p:  # Check if message is valid
        print(f"Message must be less than {p}. Exiting.")  # Warn and exit if invalid
        return
    b = random.randint(1, p - 2)  # Generate a random secret number b

    c1 = pow(g, b, p)  # Compute c1 = g^b % p
    c2 = (m * pow(e, b, p)) % p  # Compute c2 = m * (e^b % p)
    print(f"Ciphertext: (c1={c1}, c2={c2})")  # Display the ciphertext

def decryption():  # Function to decrypt a message
    if 'c1' not in globals() or 'c2' not in globals():  # Check if encryption was done
        print("Encryption must be performed first.")  # Warn if no ciphertext
        return

    x = pow(c1, a, p)  # Compute x = c1^a % p
    x_inv = pow(x, -1, p)  # Compute x^-1 modulo p (modular inverse of x)
    decrypted_message = (c2 * x_inv) % p  # Compute decrypted message = c2 * x^-1 % p
    print(f"Decrypted Message: {decrypted_message}")  # Display the decrypted message

def main():  # Main function for the program
    while True:  # Loop to allow repeated operations
        print("\nChoose an option:")  # Display menu
        print("1. Key Generation")  # Option for key generation
        print("2. Encryption")  # Option for encryption
        print("3. Decryption")  # Option for decryption
        print("4. Exit")  # Option to exit the program

        choice = input("Enter your choice: ")  # Get user's choice
        if choice == '1':  # If choice is 1
            key_generation()  # Call key generation function
        elif choice == '2':  # If choice is 2
            encryption()  # Call encryption function
        elif choice == '3':  # If choice is 3
            decryption()  # Call decryption function
        elif choice == '4':  # If choice is 4
            print("Exiting the program.")  # Exit the program
            break
        else:  # If input is invalid
            print("Invalid choice. Please try again.")  # Warn and repeat

if __name__ == "__main__":  # Run the program only if executed directly
    main()  # Call the main function
