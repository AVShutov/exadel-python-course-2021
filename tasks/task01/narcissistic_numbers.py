# count of digits in a number
def count_digits(i):
    count=0
    while i>0:
        count += 1
        i //= 10
    return count
# result for every number
def narcissistic_check(i):
    result = 0
    count = count_digits(i)
    number = i
    while i:
        digit = i % 10
        result += digit ** count
        i //= 10
    return result == number
# narcissism check
for k in range(1, 1001):
    if narcissistic_check(k):
        print (k, end=' ')
print ('\n')
