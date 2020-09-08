import re

line = "b'show hostname\n'"
print (line)
temp1 = str(line)
print (temp1)
temp2 =  re.split("\'|\n",temp1)
print (temp2)
            
