def divisors(n):
#print "Enter a number"
#n = int(raw_input())
for x in xrange(n):
	x+=1
	if n%x==0:
		print x

if __name__==__main__:
	divisors(80)
		