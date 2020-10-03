import re

# Character classes
#p = '[abc]'         # Either a or b or c
#p = '[^abc]'         # Except a or b or c
#p = '[a-z]'          # All small case alphabets
#p = '[^a-z]'
#p = '[A-Z]'           # Capital A to Z
#p = '[a-zA-Z]'          # all alphabets
#p = '[0-9]'            # only numbers
# p = '[a-zA-Z0-9]'     # Alpha neumerics
# p = '[^a-zA-Z0-9]'      # Only special characters

# Predefined character classes
# p = '\s'    # Space
# p = '\S'    # Except space
#p = '\d'     # Numbers
#p = '\D'     # Except numbers
#p = '\w'     # Alpha neumerics
#p = '\W'     # Except alpha neumerics
#p = '.'       # Everything


matcher = re.finditer(p, 'a7b@k9z ABC')
for m in matcher:
    print(m.start(), m.end(), m.group())