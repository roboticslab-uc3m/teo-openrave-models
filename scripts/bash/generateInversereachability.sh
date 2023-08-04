#!/usr/bin/env bash

openrave.py --database inversereachability --robot=../../openrave/teo_lacqueyFetch.robot.xml --manipname=trunkAndRightArm --numthreads=$(nproc)
