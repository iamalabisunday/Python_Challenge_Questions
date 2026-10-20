# Input: "aaabbc" → a3b2c1
# Input: "abcd" → a1b1c1d1
# Input: "aaa" → a3
# Input: "aabbaa" → a2b2a2

# user_input = "aaabbc"
# user_input = "abcd"
# user_input = "aaa"
# user_input = "aabbaa"


def run_len(values : str) -> str:
    if len(values) == 1:
        return values[0] + "1"
    elif not len(values):
        return ""

    record = []
    count = 1

    for index in range(1, len(values)):
        if values[index] != values[index -1]:
            record.append(values[index-1])
            record.append(str(count))
            count = 1
        else:
            count += 1
    
    record.append(values[index])
    record.append(str(count))
            
    return "".join(record)

# user_input = "adsrghj"
# user_input = "abcd"
user_input = "aaa"
# user_input = "aabbaa"

print(run_len(user_input))