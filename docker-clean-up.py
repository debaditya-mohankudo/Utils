from python_on_whales import docker

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