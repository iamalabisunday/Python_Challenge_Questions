def is_letter(ch: str) -> bool:
    return "a" <= ch <= "z" or "A" <= ch <= "Z"


def is_palindrome(text: str, left: int = 0, right: int = None):

    if right is None:
        right = len(text) - 1

    if left == right:
        return "Output: Palindrome"

    if not is_letter(text[left]):
        return is_palindrome(text, left + 1, right)

    if not is_letter(text[right]):
        return is_palindrome(text, left,  right - 1)

    if text[left].lower() != text[right].lower():
        return "Output: Not a palindrome"

    return is_palindrome(text, left + 1, right - 1)


result = is_palindrome("Was it a car or a cat I saw?")
# result = is_palindrome("Hello, World!")
print(result)
