import paramiko
import time
import getpass
import datetime
import os

c = open("config.txt","rb").readlines()
d = open("devices.txt","r")
k = open("config.txt","r").readlines()
l = open("devices.txt","r")

username = input("Username: ")
password = getpass.getpass()

print ("\n****** CONFIGURATIONS ****** \n")

for line in k:
        print (line)
print ("\n****** DEVICES ****** \n")

for line in l:
    print (line)
print ("\n-------------------------------------------------------------\n")
m=input ("\nContinue [Y/N]: ")
if m==("Y"):
    z = datetime.datetime.now()
    y = open("output.txt","a")
    y.write("+++++ TIME :: %s +++++\n\n" %(z))
    y.close()
    for line in d:

        ip_address = (line)

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip_address,username=username,password=password)

        print ("SUCCESSFULLY CONNECTED TO", ip_address)
        remote_connection = ssh_client.invoke_shell()
        h = ("%s\n*************\n\n" %(ip_address))
        i = open("output.txt","a")
        i.write(h)
        i.close()
        time.sleep(1)
        for line in c:

            #time.sleep(1)
            remote_connection.send(line)
            time.sleep(1)
            output = remote_connection.recv(65535)            
            f = open("output.txt","ab")
            f.write(output)
            f.close()
            x = open("tempout.txt","wb")
            x.write(output)
            x.close()
            os.system("cat tempout.txt")
            #time.sleep(1)
        print ("\n#############################################################################\n\n")
        time.sleep(1)
        e = ("\n\n\n#############################################################################\n\n\n")
        g = open("output.txt","a")
        g.write(e)
        g.close()
        ssh_client.close
    print ("\nPlease check the file OUTPUT.TXT to see the historical logs\n")