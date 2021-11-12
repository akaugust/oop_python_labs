import timeit
import os
import random


def file_filler(bytes_num):
    with open("Random_nums.txt", "w") as write_file:
        while os.path.getsize("Random_nums.txt") <= bytes_num:
            line = str(random.randint(1, 100)) + "\n"
            write_file.write(line)


def read_lines_file():
    sum_numbers = 0
    with open("Random_nums.txt", "r") as read_file:
        for line in read_file.readlines():
            if line.strip().isdigit():
                sum_numbers += int(line.strip())
    return sum_numbers


def for_line_file():
    sum_numbers = 0
    with open("Random_nums.txt", "r") as read_file:
        for line in read_file:
            if line.strip().isdigit():
                sum_numbers += int(line.strip())
    return sum_numbers


def generator_file():
    with open("Random_nums.txt", "r") as read_file:
        sum_numbers = (int(line.strip()) for line in read_file if line.strip().isdigit())
    return sum_numbers


if __name__ == '__main__':
    our_bytes = 50 * 1024 * 1024
    # file_filler(our_bytes)
    print(timeit.timeit(read_lines_file, number=1))
    print(timeit.timeit(for_line_file, number=1))
    print(timeit.timeit(generator_file, number=1))
