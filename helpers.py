# ----------------------------------------------------- #
# helper functions.py
'''
Here are a few useful functions! 
You will need to use these to create your puzzle. 
You may even need to include some of these in your final repository. 
''' 
# ----------------------------------------------------- #


from PyPDF2 import PdfReader, PdfWriter, PasswordType  


def make_encrypted_pdf(pdf_file_name, encryption_password, metadata = None):
    # encrypts a PDF document with any encryption password
    # optional parameter to include metadata in the PDF
    # returns True if it was successful 

    reader = PdfReader(pdf_file_name)

    writer = PdfWriter()

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Add a password to the new PDF
    # writer.encrypt(encryption_key)
    writer.encrypt(encryption_password)

    if metadata != None:
        writer.add_metadata({
                "/Author": metadata['author'],
                "/Creator": metadata['creator'],
                "/Producer": metadata['producer'],
                "/Subject": metadata['subject'],
                "/Title": metadata['title'],

            }
        )

    # Save the new PDF to a file with '_encrypted' at end of the file name
    encrypted_file_name = pdf_file_name.replace('.pdf','')+"_encrypted.pdf"
    with open(encrypted_file_name, "wb") as f:
        writer.write(f)

    return True

def decrypt_pdf(pdf_file, password):
    # returns True if the password decrypts the pdf file
    reader = PdfReader(pdf_file) 

    if reader.decrypt(password) == PasswordType.OWNER_PASSWORD:
        return True

    return False

def caesar_cipher(plain_text, encryption_key ):
    # returns the plain_text encrypted by the encryption key number

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_text = ""

    for letter in plain_text: 
        letter = letter.lower()
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            letter_encrypted_index = letter_index + encryption_key
            letter_encrypted_index = letter_encrypted_index%26
            cipher_text += alphabet[letter_encrypted_index]
        
        else:
            cipher_text += letter

    return cipher_text

def number_to_letter(number):
    # converts a number to a letter based on its position in the alphabet
    # returns the corresponding letter 

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    letter = alpha[number]

    return letter


