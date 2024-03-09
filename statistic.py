import os


def collect_statistic(numbers: list[int]) -> dict:
    subseqs = collect_subsequences(numbers)
    inc_subseq = subseqs.get("increasing")
    dec_subseq = subseqs.get("decreasing")

    sorted_numbers = sorted(numbers)

    min_value = sorted_numbers[0]
    max_value = sorted_numbers[-1]

    median_index = len(sorted_numbers) // 2
    if len(sorted_numbers) % 2 == 1:
        median_value = sorted_numbers[median_index]
    else:
        median_value = (sorted_numbers[median_index] + sorted_numbers[median_index - 1]) / 2

    avg_value = round(sum(sorted_numbers) / len(sorted_numbers), 3)

    statistic = {
        "min": min_value,
        "max": max_value,
        "median": median_value,
        "average": avg_value,
        "increasing_subseq": inc_subseq,
        "decreasing_subseq": dec_subseq,
    }
    return statistic


def collect_subsequences(numbers: list[int]) -> dict:
    std = {
        "rising": {
            "start_index": 0,
            "length": 0,
        },
        "falling": {
            "start_index": 0,
            "length": 0,
        },
        "temp": {
            "flag": None,
            "start_index": 0,
            "length": 0,
        },
    }

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            flag = "rising"

        if numbers[i] < numbers[i - 1]:
            flag = "falling"

        if numbers[i] == numbers[i - 1]:
            flag = None

        if std["temp"]["flag"] != flag:
            std["temp"] = {
                "flag": flag,
                "start_index": i - 1,
                "length": 1,
            }
            continue
        else:
            std["temp"]["length"] += 1

        if flag is None:
            continue

        if std["temp"]["length"] > std[flag]["length"]:
            std[flag]["start_index"] = std["temp"]["start_index"]
            std[flag]["length"] = std["temp"]["length"]

    inc_sub = numbers[std["rising"]["start_index"] : std["rising"]["start_index"] + std["rising"]["length"] + 1]
    dec_sub = numbers[std["falling"]["start_index"] : std["falling"]["start_index"] + std["falling"]["length"] + 1]

    subsequences = {
        "increasing": inc_sub,
        "decreasing": dec_sub,
    }
    return subsequences


def read_numbers_from_file(file_path: str) -> list[int] | None:
    if not any(
        [
            os.path.exists(file_path),
            os.path.exists(os.path.abspath(file_path)),
        ]
    ):
        print("Wrong file path.")
        return None

    with open(file_path, "r") as file:
        numbers = [int(line) for line in file.readlines()]
        # other data preparations

    return numbers


def main(path_to_file: str) -> None:
    numbers = read_numbers_from_file(path_to_file)
    if not numbers:
        return None

    statistic = collect_statistic(numbers)
    for key in statistic:
        print(f"{key}: {statistic[key]}")


if __name__ == "__main__":
    import sys

    path_to_file = sys.argv[1]
    main(path_to_file)
