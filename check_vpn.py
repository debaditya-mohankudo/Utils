import socket
import time

from rich.progress import track # pip install rich
from rich import print

duration_to_check_sec = 30

start = time.time()
while True:
	try:
		print("\033c", end="") # to clear the terminal using python (edited) 
		IPaddress=socket.gethostbyname("repo.dev.tgp.digicert.com")
		print("")
		print(f"=<>= Connected to : repo.dev.tgp.digicert.com For  {int((time.time() - start))}s")
		print("")
		for i in track(range (duration_to_check_sec), description="Sleeping..."):
			time.sleep(1)

	except socket.gaierror:
		print("\033c", end="") # to clear the terminal using python (edited) 
		start = time.time()
		print("No connection")
		time.sleep(duration_to_check_sec)
		print(f"=><= Disconnected from : repo.dev.tgp.digicert.com For {(time.time() - start)}s")
