import paramiko
import time
import getpass
import datetime
import os

# Main Paramiko Function

def login(ip_address):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip_address,username=username,password=password)

        print ("\nSUCCESSFULLY CONNECTED TO", ip_address)
        remote_connection = ssh_client.invoke_shell()
        h = ("%s\n*************\n\n" %(ip_address))
        i = open("output.txt","a")
        i.write(h)
        i.close()
        time.sleep(1)
        for line in c:

            #time.sleep(1)
            remote_connection.send(line)
            time.sleep(2)
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
        ssh_client.close()

#Sub function - Confirmation
def confirm():
        print ("-------------------------------------------------------------")
        m=input ("\nContinue [Y/N]: ")
        if m==("Y" or "y"):
                z = datetime.datetime.now()
                y = open("output.txt","a")
                y.write("+++++ TIME :: %s +++++\n\n" %(z))
                y.close()
        elif m==("N" or "n"):
                exit()
        else:
                print ("\n\nPlease type \'Y\' or \'N\'\n")
                confirm()


#Select the device

print("\n Devices ")
print("---------")
print("\n1 - Edge Devices")
print("2 - Spine, S.Leaf & Leaf")
print("3 - Spine only")
print("4 - SLeaf only")
print("5 - Leaf only")
print("6 - All LBs")
print("7 - Public LBs")
print("8 - Private LB")
print("9 - Management Switches")
print("0 - Other Devices (Specific IP)\n")
a = input("Select the device (0 to 9): ")


#Basic Inputs

c = open("config.txt","rb").readlines()
d = open ("devices.txt","r")
k = open("config.txt","r").readlines()
l = open ("devices.txt","r")

username = input("\nUsername: ")
password = getpass.getpass()

print ("\n****** CONFIGURATIONS ****** \n")
for line in k:
        print (line)


# Device if statements

print ("\n****** DEVICES ****** \n")

if a == "1":
    ltd = [*range(0,2,1)]
    for position, line in enumerate(l):
        if position in ltd:
            ip = (line)
            print (ip)    
    confirm()
    for position, line in enumerate(d):
        if position in ltd:
            ip = (line)
            login(ip)


if a == "2":
    ltd = [*range(2,26,1)]
    for position, line in enumerate(l):
        if position in ltd:
            ip = (line)
            print (ip)
    l.close()
    confirm()
    for position, line in enumerate(d):
        if position in ltd:
            ip = (line)
            login(ip)

if a == "3":
    ltd = [*range(2,5,1)]
    for position, line in enumerate(l):
        if position in ltd:
            ip = (line)
            print (ip)    
    l.close()
    confirm()
    for position, line in enumerate(d):
        if position in ltd:
            ip = (line)
            login(ip)

if a == "4":
    ltd = [*range(5,7,1)]
    for position, line in enumerate(l):
        if position in ltd:
            ip = (line)
            print (ip)    
    l.close()
    confirm()
    for position, line in enumerate(d):
        if position in ltd:
            ip = (line)
            login(ip)

if a == "5":
    ltd = [*range(7,26,1)]
    for position, line in enumerate(l):
        if position in ltd:
            ip = (line)
            print (ip)    
    l.close()
    confirm()
    for position, line in enumerate(d):
        if position in ltd:
            ip = (line)
            login(ip)

if a == "6":
    ltd = [*range(26,29,1)]
    for position, line in enumerate(l):
        if position in ltd:
            ip = (line)
            print (ip)    
    l.close()
    confirm()
    for position, line in enumerate(d):
        if position in ltd:
            ip = (line)
            login(ip)

if a == "7":
    ltd = [*range(26,28,1)]
    for position, line in enumerate(l):
        if position in ltd:
            ip = (line)
            print (ip)    
    l.close()
    confirm()
    for position, line in enumerate(d):
        if position in ltd:
            ip = (line)
            login(ip)

if a == "8":
    ltd = [*range(28,29,1)]
    for position, line in enumerate(l):
        if position in ltd:
            ip = (line)
            print (ip)    
    l.close()
    confirm()
    for position, line in enumerate(d):
        if position in ltd:
            ip = (line)
            login(ip)

if a == "9":
    ltd = [*range(29,31,1)]
    for position, line in enumerate(l):
        if position in ltd:
            ip = (line)
            print (ip)
    l.close()
    confirm()
    for position, line in enumerate(d):
        if position in ltd:
            ip = (line)
            login(ip)

if a == "0":
    while True:
        ip = input ("Enter the device IP to connect:  ")
        confirm()
        login (ip)
    
print ("\nPlease check the file OUTPUT.TXT to see the historical logs\n")
