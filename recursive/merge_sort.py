def merge(l, r, mid, arr):
  # subArrayOne = mid - l + 1
  # subArrayTwo = r - mid

  # arrLow = []
  # arrHigh = []
  # # Copy data to temp arrays leftArray[] and rightArray[]
  # for i in range(subArrayOne):
  #   arrLow.append(arr[l + i])
  # for j in range(subArrayTwo):
  #     arrHigh.append(arr[mid + 1 + j])

  arrLow = arr[l : mid]
  arrHigh = arr[mid : r]
  # print("arrLow: ", arrLow)
  print("arrHigh: ", arrHigh)
  ptrLow = 0
  ptrHigh = 0
  ptrMergedArr = l

  while (ptrLow < len(arrLow) and ptrHigh < len(arrHigh)):
    if arrLow[ptrLow] <= arrHigh[ptrHigh]:
      arr[ptrMergedArr] = arrLow[ptrLow]
      ptrLow += 1
    else:
      arr[ptrMergedArr] = arrHigh[ptrHigh]
      ptrHigh += 1
    ptrMergedArr += 1
  
  while (ptrHigh < len(arrHigh)):
    print("high")
    arr[ptrMergedArr] = arrHigh[ptrHigh]
    ptrMergedArr += 1
    ptrHigh += 1

  while (ptrLow < len(arrLow)):
    arr[ptrMergedArr] = arrLow[ptrLow]
    ptrMergedArr += 1
    ptrLow += 1
  
  print("Final result: ", arr)


def sort(l, r, arr):
  if l >= r:
    return
  
  mid = l + (r - l) // 2
  sort(l , mid, arr)
  sort(mid + 1, r, arr)
  merge(l, r, mid, arr)


def main():
  arr = [2,1,3,5,4,8]
  sort(0, len(arr), arr)
  print(arr)

main()