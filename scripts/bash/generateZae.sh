#!/usr/bin/env bash

# Authors: see AUTHORS.md at project root.
# CopyPolicy: released under the terms of the LGPLv2.1, see LICENSE at project root.
# URL: https://github.com/roboticslab-uc3m/teo-openrave-models

fileNameNoExtension="teo_lacqueyFetch"

if [ $# -eq 1 ]; then
    fileNameNoExtension="teo_$1"
fi

openrave -save $fileNameNoExtension.robot.zae ../../openrave/$fileNameNoExtension.robot.xml
