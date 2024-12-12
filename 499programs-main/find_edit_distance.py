def find_edit_distance(s1, s2):
    l1, l2 = len(s1), len(s2)
    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
    for i in range(l1 + 1):
        dp[i][0] = i
    for i in range(l2 + 1):
        dp[0][i] = i
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                del_op = dp[i][j - 1]
                replace_op = dp[i - 1][j - 1]
                insert_op = dp[i - 1][j]
                dp[i][j] = min(del_op, min(replace_op, insert_op)) + 1
    return dp[l1][l2]

if __name__ == "__main__":
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    result = find_edit_distance(s1, s2)
    print(f"\nThe minimum edit distance between '{s1}' and '{s2}' is: {result}")
