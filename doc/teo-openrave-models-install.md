## teo-openrave-models: Installation from Source Code

First install the dependencies:

- [Install CMake 3.12+](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-cmake.md)
- [Install YCM 0.11+](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-ycm.md)
- [Install YARP 3.2+](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-yarp.md)

### Install the Models

Our software integrates the previous dependencies. Note that you will be prompted for your password upon using '''sudo''' a couple of times:

```bash
cd  # go home
mkdir -p repos; cd repos  # make $HOME/repos if it does not exist; then, enter it
git clone https://github.com/roboticslab-uc3m/teo-openrave-models.git  # download teo-openrave-models software from the repository
cd teo-openrave-models; mkdir build; cd build
cmake ..
make -j$(nproc); sudo make install; cd  # go home
```

For CMake `find_package(TEO_OPENRAVE_MODELS REQUIRED)`, you may also be interested in adding the following to your `~/.bashrc` or `~/.profile`:
```bash
export TEO_OPENRAVE_MODELS_DIR=/path/to/teo-openrave-models/build
```

For additional `teo-openrave-models` options use ccmake instead of cmake.

### Generate OpenRAVE databases

```
cd  # go home
cd repos/teo-openrave-models/scripts/python
python generateConvexDecomposition.py  # Takes 1-2 min
python generateIkfast.py  # Takes aprox 10 min
```
