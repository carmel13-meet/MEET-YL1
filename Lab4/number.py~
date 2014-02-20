class Integer(object):
	def __init__(self, num, isNegative):
		self.num = num
		self.isNegative = isNegative
	def display(self):
		if self.isNegative:
			return self.num*(-1)
		else:
			return self.num		
class NegativeInteger(Integer):
	def __init__(self, num):
		Integer.__init__(self, num, True)
	def display(self):
		print "This is an object of the NegativeInteger class"
		return self.num*(-1)
if __name__ == "__main__":
	test = NegativeInteger(9)
        test2 = Integer(4, True)
	myList = [test, test2]
	for i in myList:
		print i.display()
	
