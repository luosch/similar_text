# -*- coding: utf-8 -*-

def similar_str(str1, str2):
    """
    return the len of longest string both in str1 and str2
    and the positions in str1 and str2
    """
    max_len = tmp = pos1 = pos2 = 0
    len1, len2 = len(str1), len(str2)

    for p in range(len1):
        for q in range(len2):
            tmp = 0
            while p + tmp < len1 and q + tmp < len2 \
                    and str1[p + tmp] == str2[q + tmp]:
                tmp += 1

            if tmp > max_len:
                max_len, pos1, pos2 = tmp, p, q

    return max_len, pos1, pos2


def similar_char(str1, str2):
    """
    return the total length of longest string both in str1 and str2
    """
    max_len, pos1, pos2 = similar_str(str1, str2)
    total = max_len

    if max_len != 0:
        if pos1 and pos2:
            total += similar_char(str1[:pos1], str2[:pos2])

        if pos1 + max_len < len(str1) and pos2 + max_len < len(str2):
            total += similar_char(str1[pos1 + max_len:], str2[pos2 + max_len:]);

    return total


def similar_text(str1, str2, option='normal'):
    """
    return a float value in [0, 100], which stands for match level
    """
    if len(str1) == 0 and len(str2) == 0:
        return 0.0
    elif option == 'normal':
        return similar_char(str1, str2) * 200.0 / (len(str1) + len(str2))
    elif option == 'fast':
        return 100.0 - edit_distance(str1, str2) * 200.0 / (len(str1) + len(str2))
    else:
        raise ValueError("no such option")


def edit_distance(str1, str2):
    m, n = len(str1) + 1, len(str2) + 1
        
    if m == 1 or n == 1:
        return max(m, n) - 1
    
    dp = [[0 for _ in range(n)] for __ in range(m)]
    
    for i in range(m):
        dp[i][0] = i
    
    for i in range(n):
        dp[0][i] = i
    
    for i in range(1, m):
        for j in range(1, n):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
    
    return dp[-1][-1]
