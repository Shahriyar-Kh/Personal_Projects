import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import DES
from base32hex import b32encode, b32decode
import hashlib

def encrypt():
    plain_text = plain_text_entry.get()
    password = password_entry.get()

    # Ensure plain_text and password are not empty
    if not plain_text or not password:
        messagebox.showerror("Error", "Please enter plain text and password")
        return

    # Define salt and create key using MD5 hash
    salt = b'\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
    key = (password + salt.decode('latin1')).encode('utf-8')
    m = hashlib.md5(key)
    des_key = m.digest()

    # Create DES object
    des = DES.new(des_key[:8], DES.MODE_CBC, des_key[8:])

    # Padding plain text
    pad_length = 8 - len(plain_text) % 8
    padded_plain_text = plain_text + chr(pad_length) * pad_length

    # Encrypt the plain text
    ciphertext = des.encrypt(padded_plain_text.encode('utf-8'))
    encoded_ciphertext = b32encode(ciphertext).decode('utf-8')

    # Display the encoded cipher text
    cipher_text_entry.delete(0, tk.END)
    cipher_text_entry.insert(0, encoded_ciphertext)

def decrypt():
    encoded_ciphertext = cipher_text_entry.get()
    password = password_entry.get()

    # Ensure encoded_ciphertext and password are not empty
    if not encoded_ciphertext or not password:
        messagebox.showerror("Error", "Please enter cipher text and password")
        return

    # Define salt and create key using MD5 hash
    salt = b'\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
    key = (password + salt.decode('latin1')).encode('utf-8')
    m = hashlib.md5(key)
    des_key = m.digest()

    # Create DES object
    des = DES.new(des_key[:8], DES.MODE_CBC, des_key[8:])

    # Decode the encoded cipher text
    try:
        ciphertext = b32decode(encoded_ciphertext.encode('utf-8'))
    except:
        messagebox.showerror("Error", "Invalid encoded cipher text")
        return

    # Decrypt the cipher text
    decrypted_text = des.decrypt(ciphertext)
    pad_length = decrypted_text[-1]

    # Remove padding and convert to string
    plain_text = decrypted_text[:-pad_length].decode('utf-8')

    # Display the plain text
    plain_text_entry.delete(0, tk.END)
    plain_text_entry.insert(0, plain_text)

# Create the main application window
window = tk.Tk()
window.title("DES Algorithm Interface")

# Create labels and text fields
tk.Label(window, text="Plain Text:").grid(row=0, column=0, padx=10, pady=10)
plain_text_entry = tk.Entry(window, width=30,font="Lucida 14 bold",bg="lightyellow")
plain_text_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(window, width=30, show='*',font="Lucida 14 bold",bg="lightyellow")
password_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(window, text="Cipher Text:").grid(row=2, column=0, padx=10, pady=10)
cipher_text_entry = tk.Entry(window, width=30,font="Lucida 14 bold",bg="lightyellow")
cipher_text_entry.grid(row=2, column=1, padx=10, pady=10)

# Create buttons for encryption and decryption
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt,font="Lucida 13 bold",bg="blue",cursor="hand2",fg="white")
encrypt_button.grid(row=3, column=0, columnspan=2, pady=10, sticky='ew')

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt,font="Lucida 13 bold",bg="green",cursor="hand2",fg="white")
decrypt_button.grid(row=4, column=0, columnspan=2, pady=10, sticky='ew')

# Run the application
window.mainloop()