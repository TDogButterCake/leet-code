def common_prefix(words):
    for i in range(len(words[0])):
        char = words[0][i]
        for word in words[1:]:
            if char != word[i] or len(word) == i:
                return words[0][:i]


test1 = ["flower", "flow", "flight"]
print(common_prefix(test1))

test2 = ["f", "f", "f"]

print(common_prefix(test2))
