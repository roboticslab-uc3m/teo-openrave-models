#!/usr/bin/env bash

openrave.py --database convexdecomposition --robot=../../openrave/teo_lacqueyFetch.robot.xml --numthreads=$(nproc)
