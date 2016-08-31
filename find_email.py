#coding=UTF-8
import fileinput, re
pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]+', re.IGNORECASE)
addresses = set()
for line in fileinput.input("myemail.eml"): #input不传参数则需要在执行时传递文件名参数 
	for address in pat.findall(line):
		addresses.add(address)

for address in sorted(addresses):
	print address

print "==========="
