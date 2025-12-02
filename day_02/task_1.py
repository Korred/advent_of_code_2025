with open("input.txt", "r") as file:
    text_ranges = file.read().strip().split(",")
    ranges = [tuple(map(int, text_range.split("-"))) for text_range in text_ranges]


invalid_ids_sum = 0
for start, end in ranges:
    for number in range(start, end + 1):
        str_number = str(number)
        # Skip uneven numbers
        if len(str_number) % 2 != 0:
            continue

        # Split in half
        first_half = str_number[: len(str_number) // 2]
        second_half = str_number[len(str_number) // 2 :]

        if first_half == second_half:
            invalid_ids_sum += number


print(invalid_ids_sum)
