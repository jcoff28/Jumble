import sys
if len(sys.argv) != 2:
	print('Usage: jumble.py <jumble string>')
string = sys.argv[1].strip()
stringLen = len(string)

#Add words of equal or lesser size to set. (research said that the Python set was fastest data structure for membership testing so I'm working off of that assumption)
words = set(x.strip() for x in open("wordList.txt") if len(x.strip()) <= stringLen)

#List of words to return
retList = []

#Recursive function to create every permutation with the given letters and check membership
def checkPerm(wordSoFar, lettersToUse):
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
		if lettersToUse[i] == c:
			i+=1
			continue
		c = lettersToUse[i]
		checkPerm(wordSoFar+c, lettersToUse[:i] + lettersToUse[i+1:])
		i+=1

def jumble(s):
	checkPerm("", ''.join(sorted(s.strip())))	
	
#Initial function call with the string passed in via command line
jumble(string)

#Remove the initial string from the list
if string in retList:
	retList.remove(string)

#print the list
for retString in retList:
	print(retString)



