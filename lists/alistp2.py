#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From '
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
#Then print out a count at the end.

#fn=input("Enter file name : ") or fh=open(fn) or fh=open(fn,'r') or try and except
fh=open('mbox-short.txt')
inp=fh.read()
fh.seek(0)
count=0
for line in fh:
    line=line.rstrip()
    if not line.startswith('From:'):         #do not miss ' ' in From
        continue                             #discard not from statements or skips
    else:
        #print(line)                   #strings from file,     From: stephen.marquard@uct.ac.za...
        count=count+1
        sentence=line.split()         #creates list of strings ['From:', 'stephen.marquard@uct.ac.za']
        #print(sentence)              #displayed above
        print(sentence[1])            #displays 1st element of list
print("There were", count, "lines in the file with From as the first word")
