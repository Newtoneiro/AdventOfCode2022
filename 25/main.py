import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

SNAFU_TO_DEC = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2,
}
DEC_TO_SNAFU = {v: k for k, v in SNAFU_TO_DEC.items()}


def main():
    inputs = []
    with open(filename) as f:
        for line in f.readlines():
            inputs.append(line.strip())

    def snafu_to_dec(snafu):
        total = 0
        n = len(snafu) - 1

        for i, val in enumerate(snafu):
            total += 5**(n - i)*SNAFU_TO_DEC[val]
        return total

    def dec_to_snafu(dec):
        if dec == 0:
            return "0"

        result = []

        while dec != 0:
            dec, rem = divmod(dec, 5)

            if rem > 2:
                rem -= 5
                dec += 1

            result.append(DEC_TO_SNAFU[rem])

        return "".join(reversed(result))

    total = 0
    for snafu in inputs:
        total += snafu_to_dec(snafu)
    print(dec_to_snafu(total))


if __name__ == "__main__":
    main()
