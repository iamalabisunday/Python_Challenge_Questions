def balanced_parenthese(words: str) -> str:
    count = 0
    lists = []
    for character in words:
        if character == "(" or character == "[":
            count += 1
            lists.append(character)
        elif character == ")" or character == "]":
            count -= 1
            lists.append(character)

    
    print(lists)
    if count == 0:
        for i in range(1, len(lists)):
            if lists[i] != lists[i-1]:
                return ("Output: Not Balanced") 
            else:
                return "Output: Balanced"

    else:
        return "Output: Not Balanced"
    
user_input = "(a + b) * [c - d]"  #  Balanced
# user_input = "(a + b)]" #  → Not balanced (mismatched type)
# user_input = "((a + b)"  # → Not balanced (unclosed)
# user_input = "[(a + b) * {c - d}]" # → Balanced
# user_input = "([)]" #  → Not balanced (wrong order)


result = balanced_parenthese(user_input)
print(result)