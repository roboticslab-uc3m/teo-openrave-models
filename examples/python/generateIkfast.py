##
# <b>Legal</b> 
#
# Copyright: (C) 2017 Universidad Carlos III de Madrid
#
# Author: Raul de Santos Rico
#
# CopyPolicy: Released under the terms of the LGPLv2.1 or later, see license/LGPL.TXT

from openravepy import *
from numpy import *
import numpy, time
from openravepy.misc import InitOpenRAVELogging
InitOpenRAVELogging() # initialized with a logger. Allow us to log IKFast information 

env = Environment()
env.SetViewer('qtcoin')
env.Load('/usr/local/share/teo-grasp/contexts/models/lab.env.xml')
robot = env.GetRobots()[0]
robot.SetActiveManipulator('rightArm_trunk')

ikmodel = databases.inversekinematics.InverseKinematicsModel(robot, iktype=IkParameterizationType.Transform6D)
if not ikmodel.load():
    print 'Generating IK equation of: %s (one time computation)...' %robot.GetActiveManipulator().GetName()
    ikmodel.autogenerate()
else:
    print 'Inverse Kinematic of %s loaded!' %robot.GetActiveManipulator().GetName()
