# decoder.py

def decode_message(encrypted_message):

    decoded_message = []
    
    for char in encrypted_message:
        if char.isalpha() and char.islower():  
           
            decoded_char = chr(((ord(char) - ord('a') + 3) % 26) + ord('a'))
            decoded_message.append(decoded_char)
        else:
           
            decoded_message.append(char)
    
    return ''.join(decoded_message)
