encrypt_list = []
decrypt_list = []
while True:
    user_word = input("Input: ").strip().lower()
    if not user_word.isalpha():
        print("Word Error: Enter vaild word e.g hello")
        continue
    
    user_shift = input("Shift: ").strip()
    if not user_shift.isdigit() or len(user_shift) != 1:
        print("Shift Error: Enter a single vaild number e.g 1")
        continue
    
    print("-----Choose a mode----------")
    print("1 for encrypt")
    print("2 for decrypt")
    
    user_mode = input("Mode: ").strip()
    if len(user_mode) != 1 and user_mode not in ["1", "2"]:
        print("Mode Error: enter a vaild mode - 1 or 2")
        continue
    
    if user_mode == "1":
        for character in user_word:
            new_position = (ord(character) - ord('a') + int(user_shift)) % 26
            new_character = chr(new_position + ord('a'))
            encrypt_list.append(new_character)
        print(f"Output: {"".join(encrypt_list)}")
    
    elif user_mode == "2":
        for character in user_word:
            new_position = (ord(character) - ord('a') - int(user_shift)) % 26
            new_character = chr(new_position + ord('a'))
            decrypt_list.append(new_character)
        print(f"Output: {"".join(decrypt_list)}")
        
    again  = input("Do you want to try again - y/n: ").lower().strip()
    if again != "y":
        print("Goodbye")
        break