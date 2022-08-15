import sys  #system function and perameter
import socket  #for ip and ports
from datetime import datetime  #find the date and time now

if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1]) #translate hostname to  ipv4
else:
        print("Invaliad amount of argument.")
        print("syntax: python3 scanner.py <ip>")
#add a pretty banner
print("-"*50)
print("Scanner target "+target)
print("Time started: "+str(datetime.now()))
print("-"*50)

try:
        for port in range(1,10000):
                 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                 socket.setdefaulttimeout(1)
                 result = s.connect_ex((target, port)) #return an error indicator
                 #print("checkng ports {}".format(port))
                 if result == 0:
                        print("port {} is open".format(port))
                 s.close()
except KeyboardInterrupt:
         print("\nExitting program.")
         sys.exit()
except socket.gaierror:
         print("Hostname could not be resolved")
         sys.exit()
except socket.error:
         print("couldnot connect to server")
         sys.exit()
