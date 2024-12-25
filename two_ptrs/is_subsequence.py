def is_subsequence(str1: str, str2: str) -> bool:
    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            j += 1
        i += 1
    return j == len(str2)