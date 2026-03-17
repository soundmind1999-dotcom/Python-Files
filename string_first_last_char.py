def count_special_strings(lst):
    result = []
    for word in lst:
        if len(word) >= 2 and word[0] == word[-1]:
            result.append(word)
    return result


print("Matching Strings:", count_special_strings(["aba", "xyz", "aa", "hello"]))
