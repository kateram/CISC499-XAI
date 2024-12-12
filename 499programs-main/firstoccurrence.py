def strStr(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
haystack = "hello"
needle = "ll"
result = strStr(haystack, needle)
print("The index of the first occurrence of '{}' in '{}' is: {}".format(needle, haystack, result))
