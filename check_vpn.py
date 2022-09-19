import socket
import time

while True:
	try:
		IPaddress=socket.gethostbyname("repo.dev.tgp.digicert.com")
		print("Connected, with the url: "+ "repo.dev.tgp.digicert.com"  + '-' + time.ctime())
	except socket.gaierror:
		print("No connection")
	
	time.sleep(15)
	print(int(time.time() % 100) * '-')
