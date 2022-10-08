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

import time
import typer

from psutil import Popen
from subprocess import PIPE
from typing import List, Optional



app = typer.Typer()

@app.command()
def follow_logs(container_name: Optional[str] = None) -> None:
    tail_logs_from_container(container_name)

def print_logs_from_stream(logs_stream):
    while True:
        log = logs_stream.stdout.readline()
        if len(log) != 0:
            print('-' * 20)
            print(f"{log.decode('utf-8')}") # log is in bytes
            time.sleep(.1)

def tail_logs_from_container(container_name: Optional[str] = None) -> None:
    command = [ "journalctl", 
        "--since", 
        "5 seconds ago", 
        #"--no-pager", 
        "--no-host", 
        "-u", "docker",
        "-f",
    
        #"-n", "1"
    ]

    if container_name:
        command.append( f"CONTAINER_NAME={container_name}")

    print(f"Running command: {command}")
    
    docker_logs_stream = Popen(command, stdout=PIPE)

    print_logs_from_stream(docker_logs_stream)


if __name__ == "__main__":
    app()