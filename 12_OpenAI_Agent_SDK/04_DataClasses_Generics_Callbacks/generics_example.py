# # Example without Generics
# def first_element(items):
#     return items[0]


nums = [1, 2, 3]
strings = ["a", "b", "c"]

# print(first_element(nums))  # 1
# print(first_element(strings))  # 'a'

# Issue: No type checking. We can't restrict or inform about expected data types explicitly.


# Example with Generics
from typing import TypeVar, List

# Type variable for generic typing

T = TypeVar("T")


def generic_first_element(items: List[T]) -> T:
    return items[0]


num_result = generic_first_element(nums)  # type inferred as int
string_result = generic_first_element(strings)  # type inferred as str

print(num_result)  # 1
print(string_result)  # 'a'
