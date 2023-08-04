#!/usr/bin/env bash

openrave.py --database kinematicreachability --robot=../../openrave/teo_lacqueyFetch.robot.xml --manipname=trunkAndRightArm --numthreads=$(nproc)
