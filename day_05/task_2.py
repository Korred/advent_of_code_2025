def merge_overlapping_ranges(ranges):
    if not ranges:
        return []

    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]

    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]

        if current_start <= last_end:
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))

    return merged


with open("input.txt", "r") as file:
    raw_ranges, _ = file.read().split("\n\n")
    raw_ranges = [
        tuple(map(int, line.split("-"))) for line in raw_ranges.strip().split("\n")
    ]


merged_ranges = merge_overlapping_ranges(raw_ranges)

sum_covered = sum(end - start + 1 for start, end in merged_ranges)
print(sum_covered)
