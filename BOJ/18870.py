# BOJ 18870번
n = int(input())

arr = list(map(int, input().split()))
sorted_arr = sorted(list(set(arr)))

def binary_search(target, arr, start, end):
	if start > end:
		return 0
	mid = (start + end) // 2
	if target == arr[mid]:
		return mid
	if target > arr[mid]:
		return binary_search(target, arr, mid + 1, end)
	if target < arr[mid]:
		return binary_search(target, arr, start, mid - 1)

for i in arr:
	result = binary_search(i, sorted_arr, 0, len(sorted_arr) - 1)
	print(result, end=' ')
