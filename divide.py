def divide(dividend, divisor):
    quotient = dividend / divisor
    remainder = dividend % divisor
    return quotient, remainder


a, b = divide(12, 4)

print(a, b)