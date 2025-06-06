def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals["lesson"]
    # cutted = []
    total_time = 0

    def cut_interval(intervals_list):
        """
        Функция ограничивает интервалы длительностью урока
        """
        cutted = []
        for start, end in zip(intervals_list[0::2], intervals_list[1::2]):
            start_cut = max(start, lesson_start)
            end_cut = min(end, lesson_end)
            if start_cut < end_cut:
                cutted.extend([start_cut, end_cut])
        return cutted

    # Ограничить интервалы ученика и учителя длительносью урока
    pupil_intervals = cut_interval(intervals["pupil"])
    tutor_intervals = cut_interval(intervals["tutor"])

    # Объединить пересекающиеся интервалы
    pupil_merged = merge_intervals(pupil_intervals)
    tutor_merged = merge_intervals(tutor_intervals)

    # Найти пересечение интервалов ученика и учителя
    total_cross = cross_intervals(pupil_merged, tutor_merged)

    # Посчитать время общего присутствия ученика и учителя
    for start, end in total_cross:
        total_time += end - start

    return total_time


def merge_intervals(intervals):
    """
    Функция объединяет и сортирует пересекающиеся интервалы
    """
    merged = []
    for start, end in sorted(zip(intervals[0::2], intervals[1::2])):
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged


def cross_intervals(pupil_int, tutor_int):
    """
    Функция находит пересечение двух списков интервалов
    """
    a, b = 0, 0
    result = []
    while a < len(pupil_int) and b < len(tutor_int):
        start = max(pupil_int[a][0], tutor_int[b][0])
        end = min(pupil_int[a][1], tutor_int[b][1])
        if start < end:
            result.append([start, end])
        if pupil_int[a][1] < tutor_int[b][1]:
            a += 1
        else:
            b += 1
    return result


tests = [
    {
        "intervals": {
            "lesson": [1594663200, 1594666800],
            "pupil": [
                1594663340,
                1594663389,
                1594663390,
                1594663395,
                1594663396,
                1594666472,
            ],
            "tutor": [1594663290, 1594663430, 1594663443, 1594666473],
        },
        "answer": 3117,
    },
    {
        "intervals": {
            "lesson": [1594702800, 1594706400],
            "pupil": [
                1594702789,
                1594704500,
                1594702807,
                1594704542,
                1594704512,
                1594704513,
                1594704564,
                1594705150,
                1594704581,
                1594704582,
                1594704734,
                1594705009,
                1594705095,
                1594705096,
                1594705106,
                1594706480,
                1594705158,
                1594705773,
                1594705849,
                1594706480,
                1594706500,
                1594706875,
                1594706502,
                1594706503,
                1594706524,
                1594706524,
                1594706579,
                1594706641,
            ],
            "tutor": [
                1594700035,
                1594700364,
                1594702749,
                1594705148,
                1594705149,
                1594706463,
            ],
        },
        "answer": 3577,
    },
    {
        "intervals": {
            "lesson": [1594692000, 1594695600],
            "pupil": [1594692033, 1594696347],
            "tutor": [1594692017, 1594692066, 1594692068, 15946963410],
        },
        "answer": 3565,
    },
]


if __name__ == "__main__":
    for i, test in enumerate(tests):
        test_answer = appearance(test["intervals"])
        assert test_answer == test["answer"], (
            f"Error on test case {i}, got {test_answer}, expected {test['answer']}"
        )
