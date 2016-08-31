import re
pattern = r'\*\*(.+?)\*\*(.+?)\*\*'
print re.sub(pattern, r'<em>\2</em>', '**this** **is** **it**!')

print '\\\t\\'
print r'\\\t\\'
