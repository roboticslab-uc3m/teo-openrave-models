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

    robot.SetActiveManipulator('trunkAndRightArm')
    print 'Set for kinematic reachability of: %s. Change the above code line for trunkAndLeftArm, etc...' %robot.GetActiveManipulator().GetName()

    reachabilitymodel = databases.kinematicreachability.ReachabilityModel(robot)
    if not reachabilitymodel.load():
        print 'Generating kinematicreachability of: %s (one time computation)...' %robot.GetActiveManipulator().GetName()
        reachabilitymodel.autogenerate()
    else:
        print 'Could load existing kinematicreachability of %s, not generating!' %robot.GetActiveManipulator().GetName()

    # shows the result on in mayavi
    reachabilitymodel.show()

    # Can exit...
    #while 1:
    #    pass

finally:
    RaveDestroy()
