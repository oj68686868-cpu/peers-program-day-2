# Reverse Words in a String
def reverseWords(s):
    words = s.split()
    result = []
    for i in range(len(words) - 1, -1, -1):
        result.append(words[i])
    return " ".join(result)
s = input()
print(reverseWords(s))