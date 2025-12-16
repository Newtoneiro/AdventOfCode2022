import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

COORDS = [1000, 2000, 3000]
MULTIPLICATOR = 811589153


def main():
    numbers = []
    numbers_with_indexes = []
    with open(filename) as f:
        for i, line in enumerate(f.readlines()):
            num = MULTIPLICATOR * int(line.strip())
            numbers_with_indexes.append([num, i])
            numbers.append(num)

    for _ in range(10):
        for i, val in enumerate(numbers):
            pivot_i = numbers_with_indexes[i][1]
            new_i = (pivot_i + val) % (len(numbers) - 1)
            if new_i == 0:
                new_i = len(numbers) - 1
            numbers_with_indexes[i][1] = -1

            new_numbers_with_indexes = []
            for (num, prev_num_i) in numbers_with_indexes:
                if prev_num_i == -1:
                    new_numbers_with_indexes.append([num, new_i])

                elif new_i > pivot_i and pivot_i < prev_num_i <= new_i:
                    new_numbers_with_indexes.append([num, prev_num_i - 1])

                elif new_i < pivot_i and new_i <= prev_num_i < pivot_i:
                    new_numbers_with_indexes.append([num, prev_num_i + 1])

                else:
                    new_numbers_with_indexes.append([num, prev_num_i])
            numbers_with_indexes = new_numbers_with_indexes

    output = [t[0] for t in sorted(numbers_with_indexes, key=lambda t: t[1])]
    zero_idx = [t[1] for t in numbers_with_indexes if t[0] == 0][0]

    total = 0
    for coord in COORDS:
        nth_idx = (zero_idx + coord) % len(numbers)
        total += output[nth_idx]
    print(total)


if __name__ == "__main__":
    main()
