# also called edit distance


def levenshtein_distance(str1: str, str2: str):
    dp = [[j for j in range(len(str1)+1)] for _ in range(len(str2)+1)]
    for i in range(len(str2)):
        dp[i][0] = i
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if str1[j-1] == str2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

str1 = "abc"
str2 = "yabd"

print(levenshtein_distance(str1, str2))
