sum1 = 0

for i in range(1, 101):
    sum1 = sum1 + i*i
print('sum1', sum1)

sum2 = 0

for j in range(1, 101):
    sum2 = sum2 + j
print('sum2', sum2)

sum3 = 0
sum3 = sum2 * sum2
print('sum3', sum3)

diff = 0
diff = sum3 - sum1
print('difference', diff)
