import sys
#if the user entered string on command line, use that else ask for input
if len(sys.argv) >= 2:
	string = sys.argv[1].strip()
else:
	string = raw_input('Enter jumble string: ')

stringLen = len(string)

#Add words of equal or lesser size to set. (research said that the Python set was fastest data structure for membership testing so I'm working off of that assumption)
words = set(x.strip() for x in open("wordList.txt") if len(x.strip()) <= stringLen)

#List of words to return
retList = []

#Recursive function to create every permutation with the given letters and add the ones that are english words to the list
def getWords(wordSoFar, lettersToUse):
	#if the current permutation is an English word add it to the list	
	if wordSoFar in words:
		retList.append(wordSoFar)
	#if there are no more letters to use return
	if len(lettersToUse) == 0:		
		return
	
	#iterate through all unique letters left to use, add them to the end of the current permutation, and recurse with that string and the other letters left
	i = 0
	c = ''
	while i < len(lettersToUse):
		#Wait for unique char
		if lettersToUse[i] == c:
			i+=1
			continue		
		c = lettersToUse[i]
		getWords(wordSoFar+c, lettersToUse[:i] + lettersToUse[i+1:])
		i+=1

#helper function to more easily call the recursive function
def jumble(s):
	#Call recursive function. sort the letters so function can easily iterate through unique chars as it builds the permutations
	getWords("", ''.join(sorted(s.strip())))	
	
#Initial function call with the string passed in via command line
jumble(string)

#Remove the initial string from the list
if string in retList:
	retList.remove(string)

#print the list
for retString in retList:
	print(retString)



