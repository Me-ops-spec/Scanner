import socket
from clint.textui import colored,puts_err,puts,puts_
from sys import exit
########################################
target = str(input("Entre the target: "))
#######################################
for port in range(1,8080):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.8)
    result = s.connect_ex((target, port))
    try:
        if result == 0:
            service = socket.getservbyport(port)
            puts(colored.green("The [%s:%s] Port I's Open" % (port, service)))
        else:
            service = socket.getservbyport(port)
            puts_err("The [%s:%s] I's Close" %(port, service))
    except OSError:
        continue

