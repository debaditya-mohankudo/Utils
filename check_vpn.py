import socket
import time

while True:
	IPaddress=socket.gethostbyname("repo.dev.tgp.digicert.com")
	if IPaddress=="172.16.32.100":
		print("Connected, with the IP address: "+ "repo.dev.tgp.digicert.com"  + '-' + time.ctime())
	else:
		print("No internet, your localhost is "+ "repo.dev.tgp.digicert.com" + '-' + time.ctime())
	
	time.sleep(15)
	print(int(time.time() % 100) * '-')
