def count_words(words: list[str]) -> dict[str, int]:
    punctuation = "!@#$%^&*)(_+}{,./?"
    rem_punctuation = []
    for word in words:
        if word not in punctuation:
            rem_punctuation.append(word.lower())
    clean_word = "".join(rem_punctuation)
    
    count = {}
    for word in clean_word.split():
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


def most_frequent(freq: dict[str, int]) -> str:
    words = count_words(freq)
    higher_number = None
    most_freq_word = None
    
    for word, number in words.items():
        if higher_number is None or number > higher_number:
            higher_number = number
            most_freq_word = word

    return (f"Most frequent word: {most_freq_word} ({higher_number})")
    
    
result = most_frequent("Python is fun, and Python is powerful!")
print(result)