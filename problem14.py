from datetime import datetime


def get_collatz_sequence(num):
    collatz_sequence = [num]
    while num != 1:
        if num % 2 == 0:
            num = num//2
        else:
            num = 3 * num + 1
        collatz_sequence.append(num)
    return collatz_sequence


num_seq_length_map = {}

def get_collatz_sequence_length(number):
    num = number
    sequence_length = 0
    while num != 1:
        print(num_seq_length_map)
        if num in num_seq_length_map:
            sequence_length += num_seq_length_map[num]
            break
        if num % 2 == 0:
            num = num//2
        else:
            num = 3 * num + 1
        sequence_length += 1
        num_seq_length_map[num] = sequence_length
    num_seq_length_map[number] = sequence_length
    return sequence_length


def main():
    max_l = 0
    num = 1

    for i in range(1, 10):
        l = get_collatz_sequence_length(i)
        if l > max_l:
            max_l = l
            num = i
    print(num_seq_length_map)
    print()
    print(num, max_l)


if __name__ == '__main__':
    # print(datetime.now())
    main()
    # print(get_collatz_sequence_length(50))
    # print(get_collatz_sequence_length(70))
    # print(datetime.now())
    
