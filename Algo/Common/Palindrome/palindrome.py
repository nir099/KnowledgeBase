def palindrome(str):
    for i in range(len(str)//2):
        if not str[i] == str[len(str)-1 - i]:
            return False
    return True

print(palindrome('abcba'))