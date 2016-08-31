#coding=UTF-8
#参数文件为test.txt

import fileinput, re
import types
field_pat = re.compile(r'\[(.+?)\]')

scope = {} #此处起到作用域的作用
i=0
def replacement(match):
	#print type(match)
	code = match.group(1)
	try:
		return str(eval(code, scope))
	except SyntaxError:
		exec code in scope
		return ''

lines = []
for line in fileinput.input():
	lines.append(line)
text = ''.join(lines)
print text
print type(text)

print field_pat.sub(replacement, text)
