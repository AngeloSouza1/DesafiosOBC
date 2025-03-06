def palindromo_mais_longo(s):
    n = len(s)
    if n == 0:
        return ""
    
    start, max_len = 0, 1


    dp = [[False] * n for _ in range(n)]


    for i in range(n):
        dp[i][i] = True

    for end in range(1, n):
        for begin in range(end):
            if s[begin] == s[end] and (end - begin <= 2 or dp[begin+1][end-1]):
                dp[begin][end] = True
                if end - begin + 1 > max_len:
                    max_len = end - begin + 1
                    start = begin

    return s[start:start + max_len]

entrada = "a!b@c@b!a@b#a@@@@"
print(palindromo_mais_longo(entrada))
