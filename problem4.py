def problem4(num1, num2):
    largest_palindrom = 0
    for i in range(num1, 1, -1):
        for j in range(num2, 1, -1):
            num = i * j
            if str(num) == str(num)[::-1]:
                #print(i, j)
                if num > largest_palindrom:
                    largest_palindrom = num
    return largest_palindrom
            
print(problem4(999,999))