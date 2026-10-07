def is_letter(chr) -> bool:
    if "a" <= chr <= "z" or "A" <= chr <= "Z":
        return True
    return False

def is_palindrome(text) -> bool:
    left = 0
    right = len(text)-1

    while left < right:
        if is_letter(text[left]) == False:
            left += 1

        if is_letter(text[right]) == False:
            right -= 1

        if text[left] != text[right]:
            return False
        
        left += 1
        right -= 1

        return True

input = "Was it a car or a cat I saw?"

result = is_palindrome(input.lower())

if result == True:
    print("Output: Palindrome")
else:
    print("Output: Not a palindrome")