# Question B - Find 
def total(n):
    if n < 0:
        raise ValueError("Negative Input")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + total(n - 1)

result = total(0)
print(result)


# Question D
def countdown_sum(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return countdown_sum(n-1) if n % 2 == 0 else n + countdown_sum(n-2)

print(countdown_sum(5))