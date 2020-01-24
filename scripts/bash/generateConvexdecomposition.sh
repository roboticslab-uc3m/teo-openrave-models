#!/usr/bin/env bash

# Authors: see AUTHORS.md at project root.
# CopyPolicy: released under the terms of the LGPLv2.1, see LICENSE at project root.
# URL: https://github.com/roboticslab-uc3m/teo-openrave-models

# `time ./generateConvexdecomposition.sh` with `nproc=16`: `real 0m15.307s; user 0m29.975s; sys 0m0.543s`
openrave.py --database convexdecomposition --robot=../../openrave/teo_lacqueyFetch.robot.xml --numthreads=$(nproc)
