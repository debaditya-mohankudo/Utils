import docker # pip install docker
client = docker.from_env()

# stop all containers
for container in client.containers.list():
    print('stopping...', container.name)
    container.stop()
    container.remove()
client.containers.prune()

# remove all networks
for network in client.networks.list():
    if network.name in ('none', 'bridge', 'host'):
        pass
    else:
        print('network removed', network.name)
        network.remove()
client.networks.prune()

# remove all volumes
for volume in client.volumes.list():
    print('remove volume', volume.id)
    volume.remove()
client.volumes.prune()
