import re

# p = 'a'  # Exact one match
# p = 'a+' # Atleast one match
# p = 'a*'  # any number of a's including zero
p = 'a{2}'  # 2 number of a's
matcher = re.finditer(p, 'abaabaaaab')
for m in matcher:
    print(m.start(), m.end(), m.group())