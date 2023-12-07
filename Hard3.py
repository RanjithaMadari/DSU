def countDigitOne(n):
    count = 0
    factor = 1
    i = 1


    while i <= n:
        divisor = i * 10
        count += (n // divisor) * i + min(max(n % divisor - i + 1, 0), i)
        i *= 10


    return count

n = int(input())
result = countDigitOne(n)
print(result)