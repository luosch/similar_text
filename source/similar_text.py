# -*- coding: utf-8 -*-

def similar_str(str1, str2):
    """
    return the len of longest string both in str1 and str2
    and the positions in str1 and str2
    """
    max_len = tmp = pos1 = pos2 = 0
    len1, len2 = len(str1), len(str2)
    # use str1 as base
    for p in range(len1):
        # traverse str2
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
    if option == 'normal':
        return similar_char(str1, str2) * 200.0 / (len(str1) + len(str2))
    elif option == 'fast':
        pass
    else:
        raise ValueError("no such option")


def edit_distance():
    pass

# # simple test
# if __name__ == "__main__":
#     print similar_text('aaaa', 'aaaa')
#     print similar_text('aaaa', 'aaaabbbb')
#     print similar_text('abcdef', 'aabcdefg')