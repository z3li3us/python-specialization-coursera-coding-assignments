#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
#The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
#When the program completes,sort and print the resulting words in alphabetical order.

#fn=input("Enter file name : ") or fh=open(fn) or fh=open(fn,'r') or try and except
fh=open('romeo.txt')
#create a list
wordlist=list() #or better way: wordlist=[]
inp=fh.read()
#print(inp)
#cursor at end of file
#reset to zero otherwise nothing to read, do that using:
fh.seek(0)
for line in fh:
    line=line.rstrip()
    #print(line) #same contents as fh.read() i.e string and if strip was not used then it would display contents/strings of file with extra lines
    line=line.split()  #returns list from string
    #print(line)       #prints the 4 lists got from file of strings i.e array of words
    #wrongcode: wordlist.split() as split is only used for strings not lists
    for word in line:           #for checking each element of line splitted and list got
        if word in wordlist:    #checking if word is present in our own created empty list
            continue            #if not present skip to next iteration, discards duplicates
        #alternate code would be : #if word not in wordlist:    instead of else
        else:
            wordlist.append(word)   #adding to empty list created the "word" not "line",updates list
#wrongcode words=wordlist.append(line) even this is wrong : words.append(line) as appending line would give a huge list
wordlist.sort() #according to ascii ascending or descending
print(wordlist)  #or print(sorted(wordlist))
#above statement prints list, however to print string,
## Python program to convert a list to string using list comprehension
##s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
# using list comprehension : listToStr = ' '.join([str(elem) for elem in s])
##listToStr=' '.join([str(elements) for elements in wordlist])
##print(listToStr)
