while True:
    print("---------------Caesar Cipher----------------")
    print("Shift - choose number ")
    print("choose 1 for encrypt")
    print("choose 2 for decrypt")

    user_input = input("Input(word | shift | mode): ").strip()

    try:
        words, shift, mode = user_input.split("|")
    except ValueError:
        print("Input error: use word|shift|mode, e.g. hello|3|1")
        continue

    words = words.strip().lower()
    shift = shift.strip()
    mode = mode.strip()

    try:
        shift = int(shift)
    except ValueError:
        print("Shift error: enter a number only")
        continue

    result = []

    if mode == "1":
        for character in words:
            if "a" <= character <= "z":
                current_index = ord(character) - ord("a")
                next_index = (current_index + shift) % 26
                next_char = chr(ord("a") + next_index)
                result.append(next_char)
            else:
                result.append(character)

    elif mode == "2":
        for character in words:
            if "a" <= character <= "z":
                current_index = ord(character) - ord("a")
                next_index = (current_index - shift) % 26
                next_char = chr(ord("a") + next_index)
                result.append(next_char)
            else:
                result.append(character)

    else:
        print("Mode error: enter a mode number only e.g. 1 - encrypt or 2 - decrypt")
        continue

    print("".join(result))
