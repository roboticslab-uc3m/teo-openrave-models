FROM ubuntu:24.04 AS build

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
        wget \
        unzip \
        ca-certificates \
        build-essential \
        cmake \
        libtinyxml-dev \
        libeigen3-dev \
        libboost-dev \
        libboost-filesystem-dev \
        libboost-system-dev \
        libboost-thread-dev \
        libboost-iostreams-dev \
        libxml2-dev \
        liblapack-dev \
        libsoqt520-dev \
        libcoin-dev \
        libcollada-dom-dev \
        libode-dev

ARG YARP_TAG=master

RUN wget -O rapidjson.zip https://github.com/Tencent/rapidjson/archive/master.zip && \
    wget -O openrave.zip https://github.com/rdiankov/openrave/archive/master.zip && \
    wget -O ycm-cmake-modules.zip https://github.com/robotology/ycm-cmake-modules/archive/master.zip && \
    wget -O yarp.zip https://github.com/robotology/yarp/archive/$YARP_TAG.zip && \
    wget -O yarp-devices.zip https://github.com/asrob-uc3m/yarp-devices/archive/master.zip && \
    wget -O openrave-yarp-plugins.zip https://github.com/roboticslab-uc3m/openrave-yarp-plugins/archive/master.zip && \
    wget -O teo-openrave-models.zip https://github.com/roboticslab-uc3m/teo-openrave-models/archive/master.zip

RUN unzip rapidjson.zip && \
    unzip openrave.zip && \
    unzip ycm-cmake-modules.zip && \
    unzip yarp.zip && \
    unzip yarp-devices.zip && \
    unzip openrave-yarp-plugins.zip && \
    unzip teo-openrave-models.zip

ARG CORES=1

RUN cmake -S rapidjson-master -B rapidjson-master/build \
        -DRAPIDJSON_BUILD_DOC:BOOL=OFF \
        -DRAPIDJSON_BUILD_EXAMPLES:BOOL=OFF \
        -DRAPIDJSON_BUILD_TESTS:BOOL=OFF && \
    cmake --build rapidjson-master/build --target install

RUN cmake -S openrave-master -B openrave-master/build \
        -DOPT_VIDEORECORDING:BOOL=OFF \
        -DOPT_PYTHON:BOOL=OFF \
        -DOPT_PYTHON3:BOOL=OFF \
        -DOPT_MSGPACK:BOOL=OFF \
        -DOPT_ENCRYPTION:BOOL=OFF && \
    cmake --build openrave-master/build --target install -- -j$CORES

RUN cmake -S ycm-cmake-modules-master -B ycm-cmake-modules-master/build && \
    cmake --build ycm-cmake-modules-master/build --target install

RUN cmake -S yarp-$YARP_TAG -B yarp-$YARP_TAG/build \
        -DSKIP_ACE:BOOL=ON && \
    cmake --build yarp-$YARP_TAG/build --target install -- -j$CORES

RUN cmake -S yarp-devices-master -B yarp-devices-master/build && \
    cmake --build yarp-devices-master/build --target install -- -j$CORES

RUN cmake -S openrave-yarp-plugins-master -B openrave-yarp-plugins-master/build && \
    cmake --build openrave-yarp-plugins-master/build --target install -- -j$CORES

RUN cmake -S teo-openrave-models-master -B teo-openrave-models-master/build && \
    cmake --build teo-openrave-models-master/build --target install

FROM ubuntu:24.04
COPY --from=build /usr/local /usr/local

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libtinyxml2.6.2v5 \
        libboost-filesystem1.83.0 \
        libboost-thread1.83.0 \
        libxml2 \
        liblapack3 \
        libsoqt520t64 \
        libcoin80t64 \
        libcollada-dom2.5-dp0 \
        libode8t64 && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

RUN ldconfig && \
    ln -s /usr/local/share/teo-openrave-models /openrave

VOLUME ["/root/.config/yarp/"]
VOLUME ["/openrave"]

ENV YARP_COLORED_OUTPUT=1

ENTRYPOINT ["/usr/local/bin/openrave"]
WORKDIR /openrave
