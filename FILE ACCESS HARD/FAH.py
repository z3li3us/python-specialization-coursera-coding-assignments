#filename:mbox-short.txt
fname=input("Enter file name : ")
try:
    fh=open(fname)
except:
    print("WRONG FILE")
    exit()
count=0
total=0
for line in fh:
    line=line.rstrip()
    if not line.startswith('X-DSPAM-Confidence'):
        continue
    count=count+1
    #print(line,count)
    #for x in line:
    num=float(line[19:])
    #print(num)
    total=total+num
#print(count,total,total/count)
print("Average spam confidence:",total/count)
