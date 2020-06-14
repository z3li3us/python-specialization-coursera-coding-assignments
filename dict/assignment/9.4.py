#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
fh=open('mbox-short.txt')
#or
#name = input("Enter file:")
#if len(name) < 1 :
    #name = "mbox-short.txt"
#fh = open(name) #open(name,'r')
senders=dict()   #or sender={}
for line in fh:
    if not line.startswith('From:'):  #string.startswith(value, start, end),The startswith() method returns True if the string starts with the specified value, otherwise False.
        continue                      #skips/discards
    else:
        line=line.split()
        #print(line)           #allline that start with "From:"
        emails=line[1]
        #print(emails)       #allemails in string
        emaillist=emails.split('\n') #to get back list
        #print(emaillist)
        for person in emaillist: #if it was"for person in email" it would count each letter as iteration variable and display number of times they are repeated
            senders[person]=senders.get(person,0)+1
#print(senders)
max_repeated_sender=None
repetitions=None
for sender,count in senders.items():                    #do not forget .items otherwise traceback : Valueerror:to many values to unpack
    if max_repeated_sender==None or repetitions<count: #or if max_repeated_sender is None or repetitions<count:
        max_repeated_sender=sender
        repetitions=count
##largest=-1
##for k,v in senders.items():
##    if v>largest:
##        largest=v
##        max_repeated_sender=k         #remember/capture word with most repetitions
##print(max_repeated_sender,largest)
print(max_repeated_sender,repetitions)
