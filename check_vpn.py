import socket
import time
from tqdm import tqdm # pip install tqdm
duration_to_check_sec = 30

start = time.time()
while True:
	try:
		IPaddress=socket.gethostbyname("repo.dev.tgp.digicert.com")
		print("")
		print(f"=<>= Connected to : repo.dev.tgp.digicert.com For  {(time.time() - start)}s")
		print("")
		for i in tqdm (range (duration_to_check_sec), desc="Sleeping..."):
			time.sleep(1)

	except socket.gaierror:
		start = time.time()
		print("No connection")
		time.sleep(duration_to_check_sec)
		print(f"=><= Disconnected from : repo.dev.tgp.digicert.com For {(time.time() - start)}s")
