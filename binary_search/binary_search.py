

def binary_search(arr, target):
  l = 0
  r = len(arr) - 1
  print("len: ", len(arr))
  print("target: ", target)
  while(l < r):
    mid = int((r - l) / 2  + l)
    print("index: ", mid)
    print("value: ", arr[mid])

    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      r = mid - 1
    else:
      l = mid + 1

  return -1



def main():
  arr = [33,5,7,8,9,1,10,6,4,12,15,36,45,78]
  arr.sort()

  position = binary_search(arr, 5)

  print(arr[position])

main()