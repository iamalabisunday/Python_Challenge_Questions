def is_palindrome(character: str):
    left = 0
    right = len(character)-1

    while left < right:
        
        if not character[left].isalpha():
            left += 1
            
        if not character[right].isalpha():
            right -= 1
            
        if character[left] != character[right]:
            return ("Output: Not a palindrome")
            
        left += 1
        right -= 1
        
    return ("Output: Palindrome")
    
user_input = input("Input: ").strip().lower()
words = is_palindrome(user_input)
print(words)