def merge(part1, part2):
    l = []
    pointer1 = 0
    pointer2 = 0
    while pointer1 < len(part1) and pointer2 < len(part2):
        if part1[pointer1] < part2[pointer2]:
            l.append(part1[pointer1])
            pointer1 += 1
        else:
            l.append(part2[pointer2])
            pointer2 += 1
    if pointer1 == len(part1):
        l += part2[pointer2:]
    else:
        l += part1[pointer1:]
    return l

def mergeSort(arr, left=0, right=None):
    if not right:
        right = len(arr)
    if left > right:
        return
    if len(arr) == 1:
        return arr
    elif len(arr) == 2:
        return sorted(arr)
    else:
        center = (left+right)//2
        return merge(mergeSort(arr[:center]), mergeSort(arr[center:]))
if __name__ == "__main__":
    print(merge([2,5,7], [3,9]))
    print(mergeSort([6,2,5,0,9,-69,-2, 4257932857982]))