# https://www.codingninjas.com/studio/problems/number-of-inversions_6840276?leftPanelTabValue=SUBMISSION
from typing import *

def numberOfInversions(a : List[int], n : int) -> int:
    # Write your code here.
    # Initialize the count of inversions
    count = 0

    def mergeSort(arr, low, high):
        if low == high:
            return
        
        mid = (low + high) // 2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid + 1, high)
        merge(arr, low, mid, high)

    def merge(arr, low, mid, high):
        nonlocal count
        left = low
        right = mid + 1
        temp = []

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
                count += (mid - left + 1)

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(len(temp)):
            arr[low + i] = temp[i]

    mergeSort(a, 0, n - 1)
    return count