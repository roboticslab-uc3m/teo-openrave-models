#!/usr/bin/env bash

fileNameNoExtension="teo_lacqueyFetch"

if [ $# -eq 1 ]; then
    fileNameNoExtension="teo_$1"
fi

openrave -save $fileNameNoExtension.robot.zae ../../openrave/$fileNameNoExtension.robot.xml
