def count_words(words: list[str]) -> dict[str, int]:
    feq = {}
    for word in words:
        if word in feq:
            feq[word] += 1
        else:
            feq[word] = 1
    return feq


def most_frequent(freq: dict[str, int]) -> str:
    top_word = None
    max_count = 0
    
    for word, count in freq.items():
        if count > max_count:
            max_count = count
            top_word = word
             
    return top_word

def analyze_text(text: str)-> str:
    punctuation = ".,!?;:\"'()[]>{<}"
    cleaned_text = ""
    
    for character in text.lower():
        if character not in punctuation:
            cleaned_text += character
    
    words = cleaned_text.split()
    
    words_count = count_words(words)
    top_most = most_frequent(words_count)
    
    return f"The word frequency: {top_most} {words_count[top_most]}"
            
input_text = "Python is fun, and Python is powerful!"
result = analyze_text(input_text)
print(result)