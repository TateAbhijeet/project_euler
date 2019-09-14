from mylib import fibonacci_generator


def problem2():
    sum = 0
    for i in fibonacci_generator(4000000):
        if i % 2 ==0:
            sum = sum + i
    print(sum)


if __name__ == "__main__":
    problem2()
