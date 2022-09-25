import socket
import time
from tqdm import tqdm # pip install tqdm

start = time.time()
while True:
	try:
		IPaddress=socket.gethostbyname("repo.dev.tgp.digicert.com")
		print("")
		print("Connected to : "+ "repo.dev.tgp.digicert.com"  + ' For ' + str(time.time() - start) + ' Seconds')
		print("")
		for i in tqdm (range (15), desc="Sleeping..."):
			time.sleep(1)

	except socket.gaierror:
		print("No connection")
		time.sleep(15)
