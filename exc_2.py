def find_difference(x, y):
    diff = ''
    for i in range(min(len(x), len(y))):
        if x[i] != y[i]:
            diff += x[i]
            return diff

print(find_difference("abcde", "abcd"))
