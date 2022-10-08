'''
Usage: get_logs_for_containers_journald.py [OPTIONS]

Options:
  --container-name TEXT
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

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
from typing import Optional



print(f"This is best viewd in {Fore.WHITE} BLACK COLOR BACKGROUND TERMINAL{Style.RESET_ALL}!")


app = typer.Typer()

@app.command()
def follow_logs(container_name: Optional[str] = None) -> None:
    tail_logs_from_container(container_name)

def print_in_color(color: Fore, text: str) -> None:
    print(f"{color} {text} {Style.RESET_ALL}")

def print_logs_from_stream(logs_stream: Popen, container_name: Optional[str]) -> None:
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

def tail_logs_from_container(container_name: Optional[str] = None) -> None:
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

    if container_name:
        command.append( f"CONTAINER_NAME={container_name}")

    print(f"Running command: {command}")
    
    docker_logs_stream = Popen(command, stdout=PIPE)
    print(type(docker_logs_stream))

    print_logs_from_stream(docker_logs_stream, container_name)


if __name__ == "__main__":
    app()