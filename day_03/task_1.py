def find_max_pair(bank: list[int]) -> int:
    l_max = max(bank[:-1])
    r_max = max(bank[bank.index(l_max) + 1 :])
    return l_max * 10 + r_max


with open("input.txt") as file:
    banks = [list(map(int, list(line.strip()))) for line in file.readlines()]


total_output_joltage = sum(find_max_pair(bank) for bank in banks)
print(total_output_joltage)
