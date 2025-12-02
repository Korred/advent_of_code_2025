with open("input.txt", "r") as file:
    text_ranges = file.read().strip().split(",")
    ranges = [tuple(map(int, text_range.split("-"))) for text_range in text_ranges]


def get_possible_repeating_prefixes(s):
    if len(s) == 0:
        return []

    max_prefix_length = len(s) // 2
    return [s[:i] for i in range(1, max_prefix_length + 1) if len(s) % i == 0]


invalid_ids_sum = 0
for start, end in ranges:
    for number in range(start, end + 1):
        str_number = str(number)

        # Skip numbers of len 1
        if len(str_number) == 1:
            continue

        # Uneven length numbers must use exactly one digit
        if len(str_number) % 2 != 0 and len(set(str_number)) == 1:
            invalid_ids_sum += number

        # Even length numbers must have all parts equal
        else:
            possible_prefixes = get_possible_repeating_prefixes(str_number)
            for prefix in possible_prefixes:
                repeated = prefix * (len(str_number) // len(prefix))
                if repeated == str_number:
                    invalid_ids_sum += number
                    break

print(invalid_ids_sum)
