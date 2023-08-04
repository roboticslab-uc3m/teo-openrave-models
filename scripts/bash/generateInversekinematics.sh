#!/usr/bin/env bash

openrave.py --database inversekinematics --robot=../../openrave/teo_lacqueyFetch.robot.xml --manipname=trunkAndRightArm --numthreads=$(nproc)
