def is_letter(chr) -> bool:
    return "a" <= chr <= "z" or "A" <= chr <= "Z"

def is_palindrome(text) -> bool:

    text = text.lower()
    left = 0
    right = len(text)-1

    while left < right:
        if not is_letter(text[left]):
            left += 1

        if not is_letter(text[right]):
            right -= 1

        if text[left] != text[right]:
            return False
        
        left += 1
        right -= 1

        return True

input_1 = "Was it a car or a cat I saw?"
input_2 = "Hello, World!"

result = is_palindrome(input_1)

message = print("Output: Palindrome") if result == True else print("Output: Not a palindrome")