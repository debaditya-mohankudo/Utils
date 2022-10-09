
'''Usage
python ~/workspace/Utils/get_logs_for_containers_journald.py  container_name1 contianer_name2 ...  
'''
import json
import typer
import time

from ast import For
from pyparsing import col
from colorama import Fore
from colorama import Style
from psutil import Popen
from subprocess import PIPE
from typing import Optional, List



print(f"This is best viewd in {Fore.WHITE} BLACK COLOR BACKGROUND TERMINAL{Style.RESET_ALL}!")


app = typer.Typer()

@app.command()
def follow_logs(cnames: List[str]) -> None:
    tail_logs_from_container(cnames)

def print_in_color(color: Fore, text: str) -> None:
    print(f"{color} {text} {Style.RESET_ALL}")

def print_logs_from_stream(logs_stream: Popen) -> None:
    color = Fore.WHITE
    while True:
        log = json.loads(logs_stream.stdout.readline())
        line = f"{log.get('CONTAINER_NAME', '')} {log.get('MESSAGE', '')}"
        if len(log) != 0:
            if 'INFO' in line.upper():
                color = Fore.GREEN
            elif 'WARNING' in line.upper():
                color = Fore.YELLOW
            elif 'EXCEPTION' in line.upper():
                color = Fore.RED

            print_in_color(color, line)
        else:
            time.sleep(1)

def tail_logs_from_container(container_names: List[str]) -> None:
    command = [ "journalctl", 
        "--since", 
        "5 seconds ago", 
        #"--no-pager", 
        "--no-host", 
        "-u", "docker",
        "-f",
        "-o", "json",
    
        #"-n", "1"
    ]

    for c in container_names:
        command.append( f"CONTAINER_NAME={c}")

    print(f"Running command: {command}")
    
    docker_logs_stream = Popen(command, stdout=PIPE)

    print_logs_from_stream(docker_logs_stream)


if __name__ == "__main__":
    app()