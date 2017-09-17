# 2 mutations

def find(string, target):
    c = -1
    for i in range(len(string)):
        if string[i] == target:
            c = i
    return c

if __name__ == '__main__':
    print(find("abcde", 'c'))
    print(find("aaaa", 'a'))  # duplicates
    print(find("abc", 'd'))  # what to return when not found
    print(find("", 'd')) # what to return when you have an empty string