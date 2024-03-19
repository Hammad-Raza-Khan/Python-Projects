
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
            't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(text, shift, direction):
    
    cipher_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet :
            position = alphabet.index(letter)
            how_much_shift = position + shift
            cipher_text += alphabet[how_much_shift]
        else:
            cipher_text += letter
    print(f"The {direction}d text is {cipher_text}")
        
        
continued = True 
while continued :
    from a import logos
    print(logos)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction not in ("encode", "decode"):
        print("Wrong Input! \n")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    shift = shift % 26

    ceaser(text, shift, direction)

    
    restart = input("Would you like to GO AGAIN ? type 'yes' OR 'no' \n").lower()

    while restart.lower() not in ('yes' , 'no'):
        restart = input("Enter yes/no to continue \n")
        
    if restart == "no":
        print("-----  Salam! -----")
        continued = False