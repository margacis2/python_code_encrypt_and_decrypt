import base64

# Base64 encoded string
encoded_string = input("Enter the encoded message: ")

# Decode the string from Base64 to bytes, then to the original string
decoded_bytes = base64.b64decode(encoded_string)
decoded_string = decoded_bytes.decode('utf-8')

print("Base64 Encoded:", encoded_string)
print("Decoded string:", decoded_string)
