import random  # Import the random module for generating random numbers

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:  # Numbers <= 1 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisors up to the square root of n
        if n % i == 0:  # If divisible, n is not prime
            return False
    return True  # If no divisors, n is prime

# Function to generate a random prime number
def generate_prime():
    while True:  # Keep trying until we find a prime
        num = random.randint(2, 100000)  # Generate a random number in the range
        if is_prime(num):  # Check if the number is prime
            return num  # Return the prime number

# Function to check if g is a primitive root modulo p
def is_primitive_root(g, p):
    required_set = {num for num in range(1, p)}  # All integers from 1 to p-1
    actual_set = {pow(g, exp, p) for exp in range(1, p)}  # Compute g^exp % p for all exp
    return required_set == actual_set  # g is a primitive root if both sets match

# Function to find a primitive root modulo p
def generate_primitive_root(p):
    for g in range(2, p):  # Test integers starting from 2
        if is_primitive_root(g, p):  # Check if g is a primitive root
            return g  # Return the first primitive root found

# Function to generate cryptographic keys
def key_generation():
    global p, g, a, e  # Declare variables as global to use them across functions
    p = generate_prime()  # Generate a random prime number
    print(f"Random prime number (p): {p}")  # Display the prime number
    g = generate_primitive_root(p)  # Find a primitive root modulo p
    print(f"Random primitive root modulo {p} (g): {g}")  # Display the primitive root
    a = random.randint(1, p - 2)  # Select a random private key a
    e = pow(g, a, p)  # Compute the public key e = g^a % p
    print(f"Receiver's Key: ( p={p},g={g}, e={e})")  # Display the keys

# Function to encrypt a message
def encryption():
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

# Function to decrypt a message
def decryption():
    if 'c1' not in globals() or 'c2' not in globals():  # Check if encryption was done
        print("Encryption must be performed first.")  # Warn if no ciphertext
        return

    x = pow(c1, a, p)  # Compute x = c1^a % p
    x_inv = pow(x, -1, p)  # Compute x^-1 modulo p (modular inverse of x)
    decrypted_message = (c2 * x_inv) % p  # Compute decrypted message = c2 * x^-1 % p
    print(f"Decrypted Message: {decrypted_message}")  # Display the decrypted message

# Test functions for each module
def test_is_prime():
    print("Testing is_prime...")
    if not is_prime(2):
        print("Failed: 2 should be prime.")
    if is_prime(4):
        print("Failed: 4 should not be prime.")
    if not is_prime(13):
        print("Failed: 13 should be prime.")
    if is_prime(1):
        print("Failed: 1 should not be prime.")
    if not is_prime(97):
        print("Failed: 97 should be prime.")
    print("All is_prime tests completed.")

def test_generate_prime():
    print("Testing generate_prime...")
    prime = generate_prime()
    if not is_prime(prime):
        print(f"Failed: {prime} is not prime.")
    else:
        print(f"Generated prime {prime} is valid.")
    print("All generate_prime tests completed.")

def test_is_primitive_root():
    print("Testing is_primitive_root...")
    p = 7
    if not is_primitive_root(3, p):
        print("Failed: 3 should be a primitive root of 7.")
    if is_primitive_root(2, p):
        print("Failed: 2 should not be a primitive root of 7.")
    print("All is_primitive_root tests completed.")

def test_generate_primitive_root():
    print("Testing generate_primitive_root...")
    p = generate_prime()
    g = generate_primitive_root(p)
    if not is_primitive_root(g, p):
        print(f"Failed: {g} is not a primitive root of {p}.")
    else:
        print(f"Primitive root {g} for prime {p} is valid.")
    print("All generate_primitive_root tests completed.")

def test_key_generation():
    print("Testing key_generation...")
    global p, g, a, e
    key_generation()
    if not is_prime(p):
        print(f"Failed: {p} is not a prime number.")
    if not is_primitive_root(g, p):
        print(f"Failed: {g} is not a primitive root of {p}.")
    if not (1 <= a < p - 1):
        print(f"Failed: {a} is not a valid private key.")
    if e != pow(g, a, p):
        print("Failed: Public key component e is incorrect.")
    print("All key_generation tests completed.")

def test_encryption_decryption():
    print("Testing encryption and decryption...")
    global p, g, a, e, c1, c2
    key_generation()
    message = random.randint(1, p - 1)
    print(f"Original message: {message}")
    encryption()
    if 'c1' not in globals() or 'c2' not in globals():
        print("Failed: Ciphertext was not generated.")
    decryption()
    x = pow(c1, a, p)
    x_inv = pow(x, -1, p)
    decrypted_message = (c2 * x_inv) % p
    if decrypted_message != message:
        print(f"Failed: Decrypted message {decrypted_message} does not match original {message}.")
    else:
        print("Encryption and decryption successful.")
    print("All encryption and decryption tests completed.")

# Run all tests
def all_tests():
    test_is_prime()
    test_generate_prime()
    test_is_primitive_root()
    test_generate_primitive_root()
    test_key_generation()
    test_encryption_decryption()

if __name__ == "__main__":
    all_tests()
