class Integer(object):
	def __init__(self, num, posneg):
		self.num = num
		self.posneg = posneg
	def display(self):
		if (self.posneg=="positive"):
			print self.num
		if (self.posneg=="negative"):
			print self.num - (self.num*2)

class NegativeInteger(Integer):
	def __init__(self, num): 
		super(NegativeInteger, self).__init__(num, "negative")
		

if __name__=="__main__":
	test = Integer(5, "negative")
	test.display()
	x = NegativeInteger(7)
	x.display()
