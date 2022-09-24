import socket
import time
from tqdm import tqdm # pip install tqdm

while True:
	try:
		IPaddress=socket.gethostbyname("repo.dev.tgp.digicert.com")
		print("")
		print("Connected, with the url: "+ "repo.dev.tgp.digicert.com"  + '-' + time.ctime())
		print("")
		for i in tqdm (range (15), desc="Sleeping..."):
			time.sleep(1)

	except socket.gaierror:
		print("No connection")
