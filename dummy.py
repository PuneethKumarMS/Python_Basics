from PIL import Image
import numpy as np

# Function to encrypt the image
def encrypt_image(image_path, key):
    image = Image.open(image_path)
    img_array = np.array(image, dtype=np.uint8)

    # Ensure the key is in the valid range for pixel manipulation
    key_array = np.full_like(img_array, key, dtype=np.uint8)
    encrypted_array = np.bitwise_xor(img_array, key_array)

    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save('encrypted_image.png')
    print("Image Encrypted Successfully")

# Function to decrypt the image
def decrypt_image(encrypted_image_path, key):
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_array = np.array(encrypted_image, dtype=np.uint8)

    # Use the same key to decrypt
    key_array = np.full_like(encrypted_array, key, dtype=np.uint8)
    decrypted_array = np.bitwise_xor(encrypted_array, key_array)

    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image.save('decrypted_image.png')
    print("Image Decrypted Successfully")

# Define a key (ensure it's within 0-255 range)
key = 123

# Encrypt and decrypt an image
encrypt_image('mycem.jfif', key)  # Original image
decrypt_image('mycem.jfif', key)  # Encrypted image