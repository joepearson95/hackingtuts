import sys

# Mild adapation to the original cipher algorithm to allow for system input to make it more dynamic
def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext

def main():
	print(decrypt(sys.argv[1], sys.argv[2]))

if __name__ == "__main__":
	main()
