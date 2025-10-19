from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, parts = 39, 6
    result = split_integer(value, parts)
    assert sum(result) == value


def test_difference_max_min_num() -> None:
    value, parts = 55, 3
    result = split_integer(value, parts)
    assert max(result) - min(result) == 1


def test_all_integer() -> None:
    value, parts = 32, 3
    result = split_integer(value, parts)
    assert all(isinstance(number, int) for number in result)


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(15, 3) == [5, 5, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    resalt = split_integer(321, 7)
    assert resalt == sorted(resalt)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(5, 6) == [0, 1, 1, 1, 1, 1]
