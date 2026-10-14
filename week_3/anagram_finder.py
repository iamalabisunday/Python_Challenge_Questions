def anagram(word_one, word_two):
    if len(word_one) != len(word_two):
        return "Output: Not an anagram"
    
    lists = []
    for character in word_one:
        if character in word_two:
            lists.append(character)
            
    result = "".join(lists)
    print(result)
    if word_one == result:
        return "Output: Anagram"
    
    return "Output: Not an anagram"
    
while True:
    user_input = input("Input:" ).lower().strip()
    try:
        word_one, word_two = user_input.split("|")
    except ValueError:
        print("Output: Invaild, just enter two words e.g listen | silent")
        continue
    
    print(anagram(word_one, word_two))
    
    again = input("Do you want to try agian (y/n): ").lower().strip()
    if again != "y":
        print("Goodbye")
        break