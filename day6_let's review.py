def another_order(lis):
    for word in lis:
        even = '' #парне
        odd = '' #непарне
        for index, letter in enumerate(word):
            if index % 2 == 0:
                even += str(letter)
            else:
                odd += str(letter)
        print(even, odd)

T = int(input())
lis = []
for i in range(T):
    S = str(input())
    lis.append(S)
another_order(lis)