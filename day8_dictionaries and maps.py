n = int(input())
for name in range(n):
    name_and_num = input()
    listy = name_and_num.split(' ')
    if name == 0:
        dicti = {listy[0]: listy[1]}
    else:
        dicti.update({listy[0]: listy[1]})

names = []
for i in range(n):
    name = str(input())
    names.append(name.strip())

for nam in names:
    if nam in dicti.keys():
        print(f'{nam}={dicti[nam]}')
    else:
        print('Not found')
