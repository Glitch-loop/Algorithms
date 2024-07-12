def binary_search(arr, target):
  l = 0
  r = len(arr)
  
  while (l < r):
    mid = int((r - l)/2 + l)

    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      l = mid + 1
    else:
      r = mid - 1

  return -1


def main():
  arr = [33,5,7,8,9,1,10,6,4,12,15,36,45,78]
  
  arr.sort()

  pos = binary_search(arr, 78)

  print(arr[pos])

main()