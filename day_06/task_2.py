from math import prod


def apply_operator(operator: str, values: list[int]) -> int:
    return sum(values) if operator == "+" else prod(values)


with open("input.txt", "r") as file:
    columns: list[str] = []

    for line in file:
        reversed_line = list(line[::-1].replace("\n", ""))

        if len(columns) == 0:
            columns = reversed_line

        else:
            for i, (left, right) in enumerate(zip(columns, reversed_line)):
                columns[i] = left + right

    # removes spaces from each column and filters out empty columns
    cleaned_columns = [col.replace(" ", "") for col in columns]
    cleaned_columns = list(filter(lambda x: x != "", cleaned_columns))


total_sum = 0
running_values: list[int] = []

for col in cleaned_columns:
    if col[-1] in ("+", "*"):
        running_values.append(int(col[:-1]))
        total_sum += apply_operator(col[-1], running_values)
        running_values = []
    else:
        running_values.append(int(col))

print(total_sum)
