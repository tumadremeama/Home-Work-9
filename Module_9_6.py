def all_variants(text):
    n = len(text)

    for i in range(n):
        yield text[i]

    for start in range(n):
        for end in range(start + 1, n + 1):
            if end - start > 1:
                yield text[start:end]


a = all_variants('abc')
for i in a:
    print(i)