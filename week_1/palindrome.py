def is_palindrome(word: str)-> str:
    backward = ""
    for character in word.lower():
        backward = character + backward
    
    if word == backward:
        return f"Output: {word} is a palindrome"
    
    return f"Output: {word} is not a palindrome"

while True:
    user_input = input("Enter a word: ").strip()

    result = is_palindrome(user_input)
    
    print("=" * 50)
    print(result)
    print("=" * 50)
    
    again = input("Do you want us to try it again: ").lower().strip()
    if again != "y":
        print("Goodbye")
        break