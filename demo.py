# 2 mutations

def find(string, target):
  for i in range(len(string)):
    if string[i] == target:
      return i
  return -1

if __name__ == '__main__':
    print(find("abcde", 'c'))
    print(find("aa", 'a'))  # duplicates
    print(find("abc", 'd'))  # what to return when not found
    print(find("", 'd')) # what to return when you have an empty string