from math import prod


def apply_operator(operator: str, values: list[int]) -> int:
    return sum(values) if operator == "+" else prod(values)


with open("input.txt", "r") as file:
    numbers: list[list[int]] = []
    operations: list[callable] = []

    for line in file:
        if line[0].isdigit():
            row_numbers = [[int(num)] for num in line.strip().split()]
            if not numbers:
                numbers = row_numbers
            else:
                for row_1, row_2 in zip(numbers, row_numbers):
                    row_1.extend(row_2)
        else:
            operations = list(map(apply_operator, line.strip().split()))

summed_results = 0
for i, operation in enumerate(operations):
    res = operation(numbers[i])
    summed_results += res

print(summed_results)
