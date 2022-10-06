'''
   ~/w/Utils    master !1 ?1  python ./docker-clean-up.py --help                                          2 ✘  virtualpython  
Usage: docker-clean-up.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  clean
  pause
  unpause

'''

from python_on_whales import docker
import typer

app = typer.Typer()


@app.command()
def pause():
    print('pause all containers')
    for container in docker.container.list(all=True):
        if container.state.status == 'running':
            docker.pause(container)


@app.command()
def unpause():
    print('unpause all containers')
    # pause all containers
    for container in docker.container.list(all=True):
        if container.state.status == 'paused':
            docker.unpause(container)

@app.command()
def clean():
    for container in docker.container.list(all=True):
        if container.state.status == 'running':
            docker.pause(container)

        # stop all containers
        for container in docker.container.list(all=True):
            print('stopping...', container.name)
            container.stop()
            container.remove()
        docker.container.prune()

        # remove all networks
        for network in docker.network.list():
            if network.name in ('none', 'bridge', 'host'):
                pass
            else:
                print('network removed', network.name)
                network.remove()
        docker.network.prune()

        # remove all volumes
        for volume in docker.volume.list():
            print('remove volume', volume.name)
            volume.remove()
        docker.volume.prune()

        # remove all images with None tag
        for image in docker.image.list():
            if image.repo_tags == []:
                print(image.repo_tags, image.size // (1024 * 1024), 'MB')
                print('removing image with no tags')
                image.remove(prune=True)
        

if __name__ == "__main__":
    app()