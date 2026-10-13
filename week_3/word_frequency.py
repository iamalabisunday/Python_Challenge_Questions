def word_frequency(words: str):
    punctuation = ",!@#$%^&*+}:|?"
    
    count = {}
    remove_punctuations = []
    for word in words.lower():
        if word not in punctuation:
            remove_punctuations.append(word)
            
    clean_input = "".join(remove_punctuations)
    
    for word in clean_input.split():
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
            
    most_frequent_word = None
    most_frequent_index = None
    for value, index in count.items():
        if most_frequent_index is None or index > most_frequent_index:
            most_frequent_index = index
            most_frequent_word = value
        
    return f"Output: Most frequent word: {most_frequent_word} ({most_frequent_index})"
    
result = word_frequency("Python is fun, and python is powerful")
print(result)