dictionary = {}
def dictionary():
	for i in range(0, 3):
		name = raw_input("What's your name ?")
		age = raw_input("What's your age ?")
		dictionary.update({"Name #" + str(i): name, age})

if __name__=="__main":
	 dictionary()
