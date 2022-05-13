import socket
import time



settings = {}
ports = [9000, 1192, 443, 10250]
settings["timeout"] = 5
settings["port"] = 1192
host = "private-dns-47e2c6a9.ed47d202-8d8e-4479-bc9e-cd0e48191ce4.privatelink.northeurope.azmk8s.io"



connected = False
for n in ports:
try:
tsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tsock.settimeout(settings['timeout'])
print("Checking conneectivity to: ", n)
tsock.connect((host, n))
connected = True
print("Success")
tsock.shutdown(socket.SHUT_RDWR)
tsock.close()
time.sleep(1)
print("============================")
except ConnectionRefusedError:
print('Error Refused')
print("===========================")
time.sleep(1)
except:
print("Other error")
print("++++++++++++++++++++++++++++")
time.sleep(1)