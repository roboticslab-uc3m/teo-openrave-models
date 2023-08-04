#!/usr/bin/env python

from openravepy import *
from openravepy.misc import *

try:
    RaveInitialize()
    InitOpenRAVELogging()  # From misc, handles: No handlers could be found for logger "openravepy.databases.convexdecomposition"

    env = Environment()
    #env.SetViewer('qtcoin')  # Viewer not really required...
    env.Load('../../openrave/teo_lacqueyFetch.robot.xml')

    robot = env.GetRobots()[0]

    robot.SetActiveManipulator('trunkAndRightArm')
    print 'Set for ikfast of: %s. Change the above code line for trunkAndLeftArm, etc...' %robot.GetActiveManipulator().GetName()

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
