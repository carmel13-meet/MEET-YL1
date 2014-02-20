def palindrome(word):
	for i in range(0, len(word)):
		if not word[i] == word[len(word)-1-i]:
			return False
	return True

if __name__=="__main__":
	w = raw_input("Enter a word: ")
	print palindrome(w)


