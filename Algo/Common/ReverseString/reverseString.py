def revStr(str):
    newStr = ''
    for i in range(len(str)):
        newStr += str[len(str) - 1 - i]
    return newStr

print(revStr('hello world!'))