str='123456weagwae487354gwweaghser234234'

sentinel = '====' # 遇到这个就结束
lines = []
for line in iter(input, sentinel):
    lines.append(line)

print('\n'.join(lines))

print('\n')

for line in lines:
    print(line)

print(lines)