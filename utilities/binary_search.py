from typing import List


def binary_search(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def find_min_in_sorted_pivoted_list(nums: List[int]) -> int:
    """
    This function will return the index of the minimum value

    :param nums:
    :return:
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return left


def pivoted_binary_search(nums: List[int], target: int, pivot: int) -> int:
    n = len(nums)
    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2
        rmid = (mid + pivot) % n

        if nums[rmid] == target:
            return rmid
        elif nums[rmid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
