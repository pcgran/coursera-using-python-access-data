import re

f = open('actualdata', 'r')
total = 0

for line in f:
    numbers = map(int, re.findall('[0-9]+', line))
    total += sum(numbers)
print total
