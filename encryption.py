Python 3.12.9 (tags/v3.12.9:fdb8142, Feb  4 2025, 15:27:58) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import cv2
import os

def xor_encrypt(char, key):
    return ord(char) ^ ord(key)


def encrypt_message(img, message, password):
    rows, cols, _ = img.shape
    n, m, z = 0, 0, 0
    key_length = len(password)

    if key_length == 0:
        raise ValueError("Password cannot be empty.")

    for i, char in enumerate(message):
        encrypted_value = xor_encrypt(char, password[i % key_length])
        img[n, m, z] = encrypted_value
...         z = (z + 1) % 3
...         if z == 0:
...             m += 1
...             if m == cols:
...                 m = 0
...                 n += 1
... 
...     return img
... 
... def main():
...     image_path = "DOG.png"  # Input image
...     img = cv2.imread(image_path)
... 
...     if img is None:
...         print("Error: Image not found!")
...         return
...     
...     message = input("Enter secret message: ")
...     password = input("Enter a passcode: ")
... 
...    
...     max_chars = img.shape[0] * img.shape[1] * 3
...     if len(message) > max_chars:
...         print("Error: Message too long for this image!")
...         return
... 
...   
...     encrypted_img = encrypt_message(img, message, password)
...     cv2.imwrite("encryptedImage.png", encrypted_img)
... 
...    
...     with open("key.txt", "w") as f:
...         f.write(f"{password}\n{len(message)}")
... 
...     print("\nEncryption Complete! Encrypted image saved as 'encryptedImage.png'.")
... 
... if __name__ == "__main__":
...     main()
