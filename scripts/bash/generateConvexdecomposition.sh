#!/usr/bin/env bash

# Authors: see AUTHORS.md at project root.
# CopyPolicy: released under the terms of the LGPLv2.1, see LICENSE at project root.
# URL: https://github.com/roboticslab-uc3m/teo-openrave-models

openrave.py --database convexdecomposition --robot=../../openrave/teo_lacqueyFetch.robot.xml --numthreads=$(nproc)
