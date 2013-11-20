#n = raw_input("Please enter a number: ")

#n = int(n)

#print range(1, n)

#x = range(1, n)

#for i in x:
	#if n%i == 0:
		#print i

def divisors():
	n = raw_input("n = ")
	n = int(n)
	x = range(1, n+1)
	for i in x:
		if n%i == 0:
			print i

divisors()
