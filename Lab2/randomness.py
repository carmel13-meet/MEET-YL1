from random import randint
#def Randomness():
	#answer = raw_input("Please enter h: ")
	#if answer == "h":
		#number = randint(1, 2)
		#if number == 1:
			#print "H"
		#if number == 2:
			#print "T"
#Randomness()

def Randomness():
	probability = raw_input("What's the probability you would like to use ? ")
	number = random.random()
	if number > float(probability):
		print "H"
	else:
		print "T"
		 
	
Randomness()
