import random  # Import the random module for generating random numbers

def is_prime(n):  #  this Function checks if a number is prime
    if n <= 1:  # makes sure number is not less than n 
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisors up to the square root of n
        if n % i == 0:  # If divisible, n is not prime
            return False
    return True  
def generate_prime():  # Function to generate a random prime number
    while True:  # Keep trying until we find a prime
        num = random.randint(2, 10000000)  # Generate a random number in the range given
        if is_prime(num):  # Check if the number is prime using pervious functions
            return num  

def is_primitive_root(g, p):  # Function to check if g is a primitive root modulo p
    required_set = {num for num in range(1, p)}  # All integers from 1 to p-1
    actual_set = {pow(g, exp, p) for exp in range(1, p)}  
    return required_set == actual_set  # g is a primitive root if both sets match

def generate_primitive_root(p):  # Function to find a primitive root modulo p
    for g in range(2, p):  # Test integers starting from 2 to the prime number
        if is_primitive_root(g, p):  # Check if g is a primitive root
            return g  # Return the first primitive root found

def key_generation():  # Function to generate keys
    p = generate_prime()  # Generate a random prime number
    print(f"Random prime number (p): {p}")  # Display the prime number
    g = generate_primitive_root(p)  # Find a primitive root mod  p
    print(f"Random primitive root mod {p} (g): {g}")  # Display the primitive root
    a = random.randint(1, p - 2)  # Select a random private key a
    e = pow(g, a, p)  # g ^a mod p
    print(f"Receiver's Key: ( p={p}, g={g}, e={e})")  # Display the keys
    return p, g, a, e  # Return the keys

def encryption(p, g, e):  # Function to encrypt a message
    m = int(input(f"Enter the message to encrypt (m, as an integer less than {p}): "))  # Input message
    if m >= p:  # Check if message is valid
        print(f"Message must be less than {p}. Exiting.")  # exit if invalid
        return None, None
    b = random.randint(1, p - 2)  # Generate a random secret number b
    c1 = pow(g, b, p)  # c1 = g^b % p
    c2 = (m * pow(e, b, p)) % p  #  c2 = m * (e^b % p)
    print(f"Ciphertext: (c1={c1}, c2={c2})")  # Display the ciphertext
    return c1, c2  # Return the ciphertext

def decryption(p, a, c1, c2):  # Function to decrypt a message
    x = pow(c1, a, p)  # x = c1^a % p
    x_inv = pow(x, -1, p) 
    decrypted_message = (c2 * x_inv) % p  # Compute decrypted message = c2 * x^-1 % p
    print(f"Decrypted Message: {decrypted_message}")  # Display the decrypted message

def main():  # Main function for the program
    keys_generated = False  # Flag to track if keys are generated
    p, g, a, e = 0, 0, 0, 0  # make sure variables are set to zero
    c1, c2 = 0, 0  # same thing for c1 and c2
    while True:  # Loop to allow repeated operations
        print("\nChoose an option:")  # Display menu
        print("1. Key Generation")  # Option for key generation
        print("2. Encryption")  # Option for encryption
        print("3. Decryption")  # Option for decryption
        print("4. Exit")  # Option to exit the program

        choice = input("Enter your choice: ")  # Get user's choice
        if choice == '1':  
            p, g, a, e = key_generation()  # Generate keys and store them in key generation
            keys_generated = True  # Mark keys as generated
        elif choice == '2':  
            if keys_generated:  # Check if keys are generated
                c1, c2 = encryption(p, g, e)  # Encrypt and store ciphertext
            else:
                print("Please generate keys first!")  # incase keys are not found
        elif choice == '3':  
            if c1 and c2:  # Check if ciphertext is available
                decryption(p, a, c1, c2)  # Decrypt the message
            else:
                print("Please encrypt a message first!")  # incase message not found
        elif choice == '4':  
            print("Exiting the program.")  # Exit the program
            break
        else:  # If input is invalid
            print("Invalid choice. Please try again.") 
    main()  # Call the main function
