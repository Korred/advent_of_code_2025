def find_max(bank: list[int], length: int) -> int:
    if length == 0:
        return 0

    if len(bank) == length:
        return int("".join(map(str, bank)))

    for i in range(9, 0, -1):
        try:
            idx = bank.index(i)
            remaining_bank = bank[idx + 1 :]

            if len(remaining_bank) >= length - 1:
                return i * (10 ** (length - 1)) + find_max(remaining_bank, length - 1)

        except ValueError:
            continue


with open("input.txt") as file:
    banks = [list(map(int, list(line.strip()))) for line in file.readlines()]

joltages = [find_max(bank, 12) for bank in banks]
total_output_joltage = sum(joltages)
print(total_output_joltage)
