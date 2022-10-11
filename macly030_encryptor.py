#
# File       : macly030_encryptor.py
# Author     : Lais Maciel Tarouco
# Study ID   : 110379681
# Email Id   : macly030 
# Description: Programming Assignment 2 - Caesar Cipher.
#
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

#### Defining functions:

# Function display_details.

def display_details():
    print("File       : macly030_encryptor.py")
    print("Author     : Lais Maciel Tarouco")
    print("Study ID   : 110379681")
    print("Email Id   : macly030") 
    print("Description: Programming Assignment 2 - Caesar Cipher.\n")
    print("This is my own work as defined by the University's Academic Misconduct policy.")
#

# Function get_menu_choice: displays the menu to the screen, prompts for, reads and validates the menu command entered by the user.

def get_menu_choice():

    # Display on screen a menu with comands that the user can choose.

    print("\n*** Menu ***\n")
    print("1. Encrypt string")
    print("2. Decrypt string")
    print("3. Brute force decryption")
    print("4. Quit")

    # Variable to prompt for, read menu commands from the user, initialising the loop control.
    
    option_chosen = input("\nWhat would you like to do [1,2,3,4]? ") 
   

    # Loop to validate the user entry. Display the menu until user enter options from the menu.

    while option_chosen != '1' and option_chosen != '2' and option_chosen != '3' and option_chosen != '4': 

        # Display error message on screen if user enter with invalid number.                

        print("Invalid choice, please enter either 1, 2, 3 or 4.")

        # Updating loop control. 

        option_chosen = input("\nWhat would you like to do [1,2,3,4]? ")

    # Return the value of options chosen to the program.
    
    return option_chosen
#

# Function get_offset: prompts for, reads and validates the offset entered by the user and return the offset entered by the user.

def get_offset():
         
    # Prompt user to enter with offset value and store the offeset value. 
    
    offset_user = input("Please enter offset value (1 to 94 inclusive): ")

    # Check if value entered is an integer.
    
    valid_entry = offset_user.isdigit()
      
    # Initiate a while loop to prompt user to enter with offset value if user enter with a character not an interger. 
    
    while valid_entry == False:
        offset_user = input("Please enter offset value (1 to 94 inclusive): ")
        valid_entry = offset_user.isdigit()

    if valid_entry == True:
            
        # If the value entered is an integer. Convert the string to an intereger type. 

        offset_user = int(offset_user)

        # Initiate a while loop to prompt user to enter with offset value if value entered is outside of the range 1 to 94.  

        while offset_user < 1 or offset_user > 94:
            
            offset_user = input("Please enter offset value (1 to 94 inclusive): ")
            valid_entry = offset_user.isdigit()
            offset_user = int(offset_user)
                                
        # Return the value of offset entered and validated to the program.
        
        return offset_user
#

# Function slice_string: receive a string as a parameter and return a list of printable characters to the program.

def slice_string(string):

    listChar = []           # List to store printable characters.

    # Acess each character of string and create a list where each index receives a printable character.

    for char in string:
            
        listChar += [char]
      
    return listChar
#

# Function convert_asciiCode_original: receives list of printable characters as a parameter and return a list of decimal code equivalent from the ASCII table. 

def convert_asciiCode_original(listChar):
    
    asciiCode = []           # List to store decimal equivalent codes from the ASCII table.
    
    # Acess each character of the list of printable characters and creates a list where each index receives the decimal code equivalent from the ASCII table.
    
    for index in range(len(listChar)):
         
        asciiCode.append(ord(listChar[index]))
    
    return asciiCode
#

# Function encrypt_asciiCode: receives a offset number and a list with the Ascii decimal codes from the original string to be encrypted,
# retuns a list of offset characters from the ASCII table for the encrypted string.

def encrypt_asciiCode(offset_num, asciiCode_list):
          
    ascii_encrypted = []      # List to store offset characters from the ASCII table for the encrypted string. 

    ASCII_LEN = 95             # Constant to wrap around the wrap around to the beginning of set.

    HIGHEST_DEC = 126          # Highest decimal number from the printable ASCII character set.

            
    # Acess each element of the list, subtract the current offset number and create a new list of characters from the encrypted Ascii codes.

    for item in asciiCode_list:
                    
        # Wrap around the Ascii set when arrives in the end of the list.
        
        if (item + offset_num) >  HIGHEST_DEC:
                ascii_encrypted.append(chr(item + offset_num - ASCII_LEN))

        else:    
            ascii_encrypted.append(chr(item + offset_num))

    return ascii_encrypted
#

# Function decrypt_asciiCode: receives a offset number and a list with the Ascii decimal codes from the original string to be decrypted,
# retuns a list of offset characters from the ASCII table for the decrypted string.

def decrypt_asciiCode(offset_num, asciiCode_list):
          
    ascii_decrypted = []       # List to store offset characters from the ASCII table for the decrypted string.

    ASCII_LEN = 95             # Constant to wrap around the wrap around to the beginning of set.

    LOWEST_DEC = 32            # Lowest decimal number from the printable ASCII character set.

        
    # Acess each element of the list, subtract the current offset number and create a new list of characters from the decrypted Ascii codes.
    
    for item in asciiCode_list:
                    
        # Wrap around the Ascii set when arrives in the begining of the list.
        
        if (item - offset_num) <  LOWEST_DEC:
                ascii_decrypted.append(chr(item - offset_num + ASCII_LEN))

        else:    
            ascii_decrypted.append(chr(item - offset_num))

    return ascii_decrypted
#

# Function charList_toString: receives a list of characters and return a string. 

def charList_toString(listChar):

    string1 = '' 

    for char in listChar:
            
        string1 += char

    return string1
#

# Function bruteForce_decrypt: receives a list of the Ascii decimal codes from the original string to be decrypted. Returns with a list of the 94 possible decrypted strings.  

def bruteForce_decrypt(asciiCode_list):

    current_offset = 1         # Variable to count the numbers of loop - loop control. 
                 
    list_decryptedChars = []   # List to store offset characters from the ASCII table for the decrypted string.

    list_bruteForce = []       # List to store all 94 possible decrypted strings.

    ASCII_LEN = 95             # Constant to wrap around the wrap around to the beginning of set.

    LOWEST_DEC = 32            # Lowest decimal number from the printable ASCII character set.

    MAX_OFFSET = 94            # Maximum quantity of possible decrypted strings.


    # Start the while loop and run the while suite until the number maximum of possibilities = 94.
    # Acess each element of the list, subtract the current offset number and create a new list of characters from the decrypted Ascii codes.

    while current_offset <= MAX_OFFSET:
                         
        for item in asciiCode_list:
                            
            # Wrap around the Ascii set when arrives in the begining of the list.
            
            if (item - current_offset) <  LOWEST_DEC:
                list_decryptedChars.append(chr(item - current_offset + ASCII_LEN))
                        
            else:
                list_decryptedChars.append(chr(item - current_offset))                                              
                    
        # Call function charList_toString to generate a string out of the character's list. 
        
        brute_str = charList_toString(list_decryptedChars)
        
        # Create a list of the decrypted strings generated. 

        list_bruteForce.append(brute_str)

        # Update the loop control.
        
        current_offset += 1 
         
        # Update the list of offset characters to start a new list with another possible decrypted character list in the new loop. 
        
        list_decryptedChars = []     

    # Return the with a list of all the decrypted strings generated.

    return list_bruteForce
        
# Function display_BruteForceResults: receives a list of all the decrypted strings generated and print it to screen with appropriate message. 

def display_BruteForceResults(list_bruteForce):

    print(end = '\n')
    
    # Acess each index of the list, and print the offset and the correspondent string. 
    
    for index in range(len(list_bruteForce)):
            
            print("Offset:",(index + 1) ,"= Decrypted string:",list_bruteForce[index])


#### Declaring constants:

    
ASCII_LEN = 95             # Constant to wrap around the wrap around to the beginning of set.

LOWEST_DEC = 32            # Lowest decimal number from the printable ASCII character set.

HIGHEST_DEC = 126          # Highest decimal number from the printable ASCII character set.

MAX_OFFSET = 94            # Maximum quantity of possible decrypted strings.
    
    

#### Starting the Program: 
            
            
# Display details of the Assignment, name and ID. 

display_details ()

# Call the function to display the menu of comands and prompt use to enter with their choice. 

choice = get_menu_choice()  # Variable to store the command chosen by the user from the menu. Initiate the while loop. 
   
    
# Start the while loop and process the commands if the choices are 1 or 2 or 3:

while choice == '1' or choice == '2' or choice == '3':

    # Process the command 1 from the menu: encrypt the string.
    
    if choice == '1':

        # Prompt user to enter with a string to encrypt. 

        toEncrypt = input("\nPlease enter string to encrypt: ")

        # Call function to enter with offset number.

        offset = get_offset()

        # Call function to transform the string into a list of characters.

        listChar_original = slice_string(toEncrypt)

        # Call function to transform characters in the list into their corresponding Ascii decimal code. 

        asciiCode_original = convert_asciiCode_original(listChar_original)

        # Call function to access the Ascii decimal code adds offset number to it and return
        # with the character corresponding the new decimal Ascii code. .

        asciiCode_encrypted = encrypt_asciiCode(offset, asciiCode_original)

        # Call function that access all index from the list and build a new string (encrypted). 

        encrypted = charList_toString(asciiCode_encrypted)
           
        print(f"\nEncrypted string:\n{encrypted}")


    # Process the command 2 from the menu: decript the string. 

    elif choice == '2':
                       
        # Prompt user to enter with a string to decrypt.
        
        toDecrypt = input("\nPlease enter string to decrypt: ")

        # Call function to enter with offset number. 

        offset = get_offset()
        
        # Call function to transform the string into a list of characters.
        
        listChar_original = slice_string(toDecrypt)
        
        # Call function to transform characters in the list into their corresponding Ascii decimal code.

        asciiCode_original = convert_asciiCode_original(listChar_original)

        # Call function to access the Ascii decimal code subtracts the offset number from it and return
        # with the character corresponding the new decimal Ascii code.

        asciiCode_decrypted = decrypt_asciiCode(offset, asciiCode_original)

        # Call function that access all index from the list and build a new string (decrypted). 

        decrypted = charList_toString(asciiCode_decrypted)

        # Display the decrypted word on the screen.
              
        print(f"\nDecrypted string:\n{decrypted}")

                       
    # Process the command 3 from the menu: brute force decrypt the string provided.

    elif choice == '3':
        
        # Prompt user to enter with a string to decrypt.
        
        toDecrypt = input("\nPlease enter string to decrypt: ")

        # Call function to transform the string into a list of characters.

        listChar_original = slice_string(toDecrypt)

        # Call function to transform characters in the list into their corresponding Ascii decimal code.

        asciiCode_original = convert_asciiCode_original(listChar_original)

        # Call function to access the Ascii decimal code subtracts the offset number from it and return
        # with the character corresponding the new decimal Ascii code.
        # Access all index from the list and build a new string (decrypted).
        
        asciiCode_decrypted = bruteForce_decrypt(asciiCode_original)

        # Call the function to display the all the possible decrypted words on the screen (94 possible offset numbers).

        display_BruteForceResults(asciiCode_decrypted)

    # Call the function to display the menu of comands and prompt use to enter with their choice.       

    choice = get_menu_choice()


# Display message when user chose option 4 from the menu and no longer will be in the while loop above. 

print("\nGoodbye.")


