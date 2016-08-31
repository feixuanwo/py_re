import re

text = "JGood is handsome boy, he is cool, clever, and so on..."
m = re.match(r"(\w+)\s(\w+)\s", text)
if m:
	print m.group(0)
	print m.group(1)
	print m.group(2)
else:
	print 'not match'
