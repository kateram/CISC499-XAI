def countSort(arr):
    output = [0 for _ in range(len(arr))]
    count = [0 for _ in range(256)]
    ans = ["" for _ in arr]
    for i in arr:
        count[ord(i)] += 1
    for i in range(1, 256):
        count[i] += count[i - 1]
    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans


if __name__ == '__main__':
    arr = input("Enter a string to sort: ")
    ans = countSort(arr)
    print("Sorted character array is:", "".join(ans))
