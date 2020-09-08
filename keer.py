import time
import getpass
import datetime
import os

c = open("old.txt","rb").readlines()
d = open("old.txt","r").readlines()

#collect all the words next to constraints and save it in other temp variable
#Check if value of constraint is present.
#If yes, do nothing.
#If no, copy the content of the file till next keyword constraints

for line in c:
    e = str (line)
    f = e[2:12]
    #print (f)

    if (f=="constraint"):
        g = e [13:-7]
        h = ("%s\n"%(g))
        z = open("refer.txt","a")
        z.write(h)
        z.close()
        #print (h)

u = open("new.txt","rb").readlines()
v = open("new.txt","r").readlines()
y = open("refer.txt","r").readlines()
for line in y:

    #print (line)
    l = str (line)
    for line in v:
        i = str (line)
        j = i[0:10]
        #print (j)
        #k = i[13:20]
        #l = str (line)
        #m = l[13:-7]

        if (j=="constraint"):
            k = i[11:-3]
            #m = l[13:-7]
            m = l
            k = str(k)
            o = ("%s\n"%(k))
            m = str(m)
            #print ("K=")
            #print (o)
            #print ("M=")
            #print (m)
            if (m == o):
                print ("PRESENT\n")
            else:
                print ("TO WRITE TO new2\n")
                n = open("new2.txt","a")
                n.write(i)
                n.close()
