# def printList(lst):
#     for element in lst:
#         print(element)
#
# printList([3,1,2,6,4,2])
#
#
# def countLetters(chars):
#     counts = [0] * 26
#     for i in chars:
#         counts[ord(i) - ord('a')] += 1
#     return counts
#
# nums = countLetters("abcdefghijkabcd")
# for i in nums:
#     print(i)


# def binarySearch(lst,key):
#     low = 0
#     high = len(lst) - 1
#     while high >= low:
#         mid = (low + high) // 2
#         if key < lst[mid]:
#             high = mid - 1
#         elif key == lst[mid]:
#             return mid
#         else:
#             low = mid + 1
#     return -1
#
# lst = [1,4,7,12,34,45,62,90,100]
# print(binarySearch(lst,60))

# def selectionSort(lst):
#     for i in range(len(lst)-1):
#         currentMin = lst[i]
#         currentMinIndex = i
#         for j in range(i+1,len(lst)):
#             if currentMin > lst[j]:
#                 currentMin = lst[j]
#                 currentMinIndex = j
#
#         if currentMinIndex != i:
#             lst[currentMinIndex] = lst[i]
#             lst[i] = currentMin
#
# lst = [1,9,4.5,10.6,5.7,-4.5]
# selectionSort(lst)
# print(lst)

def insertionSort(lst):
    for i in range(1,len(lst)):
        currentElement = lst[i]
        k = i - 1
        while k >= 0 and lst[k] > currentElement:
            lst[k+1] = lst[k]
            k -= 1
        lst[k+1] = currentElement
lst = [1,9,4.5,10.6,5.7,-4.5]
insertionSort(lst)
print(lst)