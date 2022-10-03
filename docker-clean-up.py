from python_on_whales import docker

import argparse

parser = argparse.ArgumentParser(description='Docker clean up')
parser.add_argument('--operation', type=str, help='valid values are : clean/pause/unpause')



args = parser.parse_args()
print(args.operation)




if args.operation == 'pause':
    print('pause all containers')
    for container in docker.container.list(all=True):
        if container.state.status == 'running':
            docker.pause(container)

if args.operation == 'unpause':
    print('unpause all containers')
    # pause all containers
    for container in docker.container.list(all=True):
        if container.state.status == 'paused':
            docker.unpause(container)

if args.operation == 'clean':
    # pause all containers
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
    
