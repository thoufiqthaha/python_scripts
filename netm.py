from netmiko import ConnectHandler
import getpass
import time
import datetime

ip = "172.23.0.49"
username = "thowfeeq"
password = getpass.getpass()

arista = {"device_type":"arista_eos","ip":ip,
          "username":username,"password":password}
netcon = ConnectHandler(**arista)
output = netcon.send_command("show hostname")
print (output)
