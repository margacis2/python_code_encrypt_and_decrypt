import base64

# Original string
original_string = input("Enter the string to encode: ")

# Encode the string to bytes, then to Base64
encoded_bytes = base64.b64encode(original_string.encode('utf-8'))

# Convert bytes back to string
encoded_string = encoded_bytes.decode('utf-8')

print("Original string:", original_string)
print("Base64 Encoded:", encoded_string)
