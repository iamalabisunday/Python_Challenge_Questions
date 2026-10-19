# Input: "aaabbc" → a3b2c1
# Input: "abcd" → a1b1c1d1
# Input: "aaa" → a3
# Input: "aabbaa" → a2b2a2

# user_input = "aaabbc"
# user_input = "abcd"
# user_input = "aaa"
user_input = "aabbaa"

def run_len(value : str) -> dict:
    record = {}
    for value in value.lower():
        if value in record:
            record[value] += 1
        else:
            record[value] = 1
            
    lists = []
    for value, index in record.items():     
        lists.append(str(value))
        lists.append(str(index))
        
    return f"Input: {"".join(lists)}"

print(run_len(user_input))