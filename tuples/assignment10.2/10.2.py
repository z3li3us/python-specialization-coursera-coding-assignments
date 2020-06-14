#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list() #lst=[]
dct=dict() #dct={}
for line in handle:
    if line.startswith('From '):
        #print(line)                 #string from file starting with "From:"
        line=line.split()
        #print(line)                 #list from string split by space
        timeframe = (line[-2:-1])          #list of only timeframe
        #print(timeframe)             #list of whole timeframe 09:16:55
        #hrs=timeframe.split(':')  syntax wrong code as list cannot be split
        #time=timeframe[0]           #string of time
        #timesplit=time.split(':')    #list of hours,minutes,seconds
        #or directly above 2lines of code combine
        timesplit=timeframe[0].split(':')
        #print(timesplit)
        hrs=timesplit[0]     #string(0) of hours only
        #print(hrs)
        hrs=hrs.split()      #getting back list form a single string
        #print(hrs)
        for each in hrs:
            dct[each]=dct.get(each,0)+1
    continue #or
    #else:
        #continue
#print(dct)
#sorting by hours (keys) now
## semantic wrong code : print(sorted(dct))  #this gives only hrs not the count of how many times repeated
#print(sorted( [ (k,v) for (k,v) in dct.items() ] ) ) #direct print of the whole list
###lst = sorted( [(k,v) for (k,v) in dct.items()] )   #LIST OF TUPLES
###for tag,value in lst:
    ###print(tag,value)
#substitute of above 3 lines ### is :
lst = sorted(dct.items())   #LIST OF TUPLES
for tag,value in lst:
    print(tag,value)
