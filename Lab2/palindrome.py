def palindrome(word):
	if word == word[::-1]:
		return True
	else:
		return False

if __name__=="__main__":
	w = raw_input("Enter a word: ")
	print palindrome(w)


