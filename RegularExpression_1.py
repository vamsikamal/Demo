import re
count = 0
#pattern = re.compile('ab')
#match = pattern.finditer('abaababa')
match = re.finditer('ab', 'abaababa')

for m in match:

    count = count + 1
    print(m.start(), m.end(), m.group())

print('Number of matches occurred', count)