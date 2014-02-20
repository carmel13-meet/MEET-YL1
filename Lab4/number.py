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
	print "How many numbers do you want to create ? "
	answer = int(raw_input())
	for i in range(0, answer):
		print "Give me a number "
		yourNum = int(raw_input())
		print "Is it positive or negative ? "
		answer2 = raw_input()
		if answer2 == "positive" or answer2 == "Positive":
			x = Integer(yourNum, False)
			print x.display()
		elif answer2 == "negative" or answer2 == "Negative":
			x = NegativeInteger(yourNum)
			print x.display()
		else:
			print "-- WRONG ANSWER --"
	
