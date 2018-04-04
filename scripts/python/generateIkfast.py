#!/usr/bin/env python

# Copyright: (C) 2018 Universidad Carlos III de Madrid
# Author: Raul de Santos Rico
# CopyPolicy: Released under the terms of the LGPLv2.1 or later, see license/LGPL.TXT

from openravepy import *
from openravepy.misc import *

try:
    RaveInitialize()
    InitOpenRAVELogging()  # From misc, handles: No handlers could be found for logger "openravepy.databases.convexdecomposition"

    env = Environment()
    #env.SetViewer('qtcoin')  # Viewer not really required...
    env.Load('/usr/local/share/teo-openrave-models/contexts/openrave/teo/teo.robot.xml')

    robot = env.GetRobots()[0]
    robot.SetActiveManipulator('rightArm_trunk')

    ikmodel = databases.inversekinematics.InverseKinematicsModel(robot, iktype=IkParameterizationType.Transform6D)
    if not ikmodel.load():
        print 'Generating ikfast of: %s (one time computation)...' %robot.GetActiveManipulator().GetName()
        ikmodel.autogenerate()
    else:
        print 'Could load existing ikfast of %s, not generating!' %robot.GetActiveManipulator().GetName()

    # Can exit...
    #while 1:
    #    pass

finally:
    RaveDestroy()
