dividend = 10
divisor = -3
sign = (-1 if((dividend < 0) ^ (divisor < 0)) else 1)
dividend = abs(dividend)
divisor = abs(divisor)
num2 = divisor
num1 = 1
track = [num2, num1]
quotient = 0
i = 0
while dividend>=divisor:
    if num2>dividend:
        quotient += track[1]
        dividend = dividend-track[0]
        i = 0
    track[0] = num2
    track[1] = num1
    num1 = 1<<i
    num2 = divisor<<i
    i = i+1
print(quotient*sign)
