3D OpenRAVE models for TEO robot. If you are looking for the source code of the robot itself, visit the [teo-main](https://github.com/roboticslab-uc3m/teo-main) repository.

## Installation

Installation instructions for installing from source can be found [here](doc/teo-openrave-models-install.md).

## Docker

The following Docker images are available in the [ghcr.io container registry](https://github.com/roboticslab-uc3m/teo-openrave-models/pkgs/container/teo-openrave-models):

- `docker pull ghcr.io/roboticslab-uc3m/teo-openrave-models:latest`

TEO OpenRAVE models are already preinstalled.

### Usage

The image is configured to use the `openrave` executable as entry point and the `/usr/local/share/teo-openrave-models` path as the working directory.

First, make sure you launched the YARP server (`yarp server --write`) and gave access to the X server (`sudo xhost +`). Then, issue the following command anywhere on the preinstalled model you wish to load, e.g. `teo_lacqueyFetch.robot.xml`:

```bash
docker run --rm --privileged \
           -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
           -v $HOME/.config/yarp:/root/.config/yarp:ro \
           -e DISPLAY \
           ghcr.io/roboticslab-uc3m/teo-openrave-models:latest openrave/teo_lacqueyFetch.robot.xml
```

Alternatively, appending `-v $XAUTHORITY:/root/.Xauthority:ro` to the list of options would avoid the need of `sudo xhost +`. In .bashrc, add the following line:

`export XAUTHORITY=$(xauth info | grep "Authority file" | awk '{ print $3 }')`

**Note:** this command will NOT launch the joint controllers, just the visual/articulated model. In order to send motion commands to the simulated robot and interface with its sensors, you need to invoke the plugins (see [openrave-yarp-plugins](https://github.com/roboticslab-uc3m/openrave-yarp-plugins)). This is easier done through the helper script [`teoSim`](https://github.com/roboticslab-uc3m/teo-configuration-files/blob/master/scripts/bash/teoSim) available through the [teo-configuration-files](https://github.com/roboticslab-uc3m/teo-configuration-files) repository.

It is advised to register the following aliases in your `.bashrc`:

```bash
XAUTHORITY=$(xauth info | grep "Authority file" | awk '{ print $3 }')
alias openrave='docker run --rm --privileged -v /tmp/.X11-unix:/tmp/.X11-unix:ro -v $XAUTHORITY:/root/.Xauthority:ro -v $HOME/.config/yarp:/root/.config/yarp:ro -e DISPLAY ghcr.io/roboticslab-uc3m/teo-openrave-models:latest'
```

Now, just run `teoSim` from the terminal to launch the model with its associated controllers.

#### Developing

You might want to clone this repo and load the models you are currently working on instead of the preinstalled ones. A volume mounting point can be added on the current working directory (navigate to the path where your models are located):

```bash
docker run --rm --privileged \
           -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
           -v $HOME/.config/yarp:/root/.config/yarp:ro \
           -v $PWD:/openrave:ro \
           -e DISPLAY \
           ghcr.io/roboticslab-uc3m/teo-openrave-models:latest teo_lacqueyFetch.robot.xml
```

In .bashrc (following the previous snippet), you may want to add the following line:

```bash
alias openrave-dev='docker run --rm --privileged -v /tmp/.X11-unix:/tmp/.X11-unix:ro -v $XAUTHORITY:/root/.Xauthority:ro -v $HOME/.config/yarp:/root/.config/yarp:ro -v $PWD:/openrave:ro -e DISPLAY ghcr.io/roboticslab-uc3m/teo-openrave-models:latest'
```

### Building

The following build args are available:

- `YARP_TAG`: YARP tag/branch/commit to compile against (default: `master`)
- `CORES`: number of cores passed to the compiler (default: `1`)

Note that `YARP_TAG=yarp-3.9` was reported to cause issues ([#10](https://github.com/roboticslab-uc3m/teo-openrave-models/issues/10#issuecomment-2267623679)).

Example:

```bash
cd /path/to/teo-openrave-models/docker
docker build -t ghcr.io/roboticslab-uc3m/teo-openrave-models:latest --build-arg CORES=18 --build-arg YARP_TAG=master --file Dockerfile .
```

It is advised to use the GitHub Action `docker.yml` via manual dispatch (click on ["Run workflow"](https://github.com/roboticslab-uc3m/teo-openrave-models/actions/workflows/docker.yml)).

## Contributing

#### Posting Issues

1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. [Post an issue / Feature request / Specific documentation request](https://github.com/roboticslab-uc3m/teo-openrave-models/issues)

#### Fork & Pull Request

1. [Fork the repository](https://github.com/roboticslab-uc3m/teo-openrave-models/fork)
2. Create your feature branch (`git checkout -b my-new-feature`) off the `master` branch, following the [Forking Git workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow)
3. Commit your changes
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## Status

[![Issues](https://img.shields.io/github/issues/roboticslab-uc3m/teo-openrave-models.svg?label=Issues)](https://github.com/roboticslab-uc3m/teo-openrave-models/issues)

## Similar and Related Projects

- [roboticslab-uc3m/teo-gazebo-models](https://github.com/roboticslab-uc3m/teo-gazebo-models)
