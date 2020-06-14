# Use words.txt as the file name
#changing contents to uppercase
fname = input("Enter file name: ")
try:
    fh = open(fname,'r')
except:
    print("Bad file name")
    quit()
for line in fh:
    line=line.rstrip()
    print(fh.read().upper())
