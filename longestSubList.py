def count_long_subarray(array):
    array = list(array)
    subArrays = []
    for i in range(len(array)):
        endIndex = i
        counter = 1
        while endIndex+1 < len(array):
            if array[endIndex+1] > array[endIndex]:
                counter += 1
                endIndex += 1
            else:
                break
        subArrays.append(counter)
    return subArrays.count(max(subArrays))
if __name__ == "__main__":
    print(count_long_subarray((1,3,4,2,7,5,6,9,2)))