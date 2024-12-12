def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    ans = ""
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]
    
    return ans

strs = ["flower", "flow", "flight"]
result = longestCommonPrefix(strs)
print("Longest Common Prefix:", result)