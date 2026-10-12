def list_traget(list_num: list, target: int):
    for index, value in enumerate(list_num):
        if target in list_num and value == target:
            return f"The index of {target}: {index}"
        else: 
            f"The index of {target}: Not Found"


values = [14, 7, 22, 9, 7, 31]
target = 22
result = list_traget(values, target)
print(result)
