
import socket
import time
import typer

from rich.progress import track # pip install rich
from rich import print

duration_to_check_sec = 30

def test_connection(site: str) -> None: 
	start = time.time()
	while True:
		try:
			print("\033c", end="") # to clear the terminal using python (edited) 
			IPaddress=socket.gethostbyname(site)
			print(f"=<>= Connected to : {site} For  {int((time.time() - start))}s")
			for i in track(range (duration_to_check_sec), description="Sleeping..."):
				time.sleep(1)

		except socket.gaierror:
			print("\033c", end="") # to clear the terminal using python (edited) 
			print("No connection")
			time.sleep(duration_to_check_sec)
			start = time.time()
			print(f"=><= Disconnected from : {site}")

if __name__ == "__main__":
	typer.run(test_connection)