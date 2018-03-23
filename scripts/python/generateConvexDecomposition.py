#!/usr/bin/env python

import openravepy
from openravepy import *

try:
    RaveInitialize()

    env=Environment()
    env.SetViewer('qtcoin')
    env.Load('/usr/local/share/teo-openrave-models/contexts/openrave/teo/teo.robot.xml')

    # Convex Decomposition
    teo_robot = env.GetRobots()[0]
    cdmodel = databases.convexdecomposition.ConvexDecompositionModel(teo_robot, padding=0.02)  # Else defaults to zero padding

    if not cdmodel.load(): 
        # If not already in the database. Generate:
        print 'ConvexDecomposition not found, generating (allow 1-2 min)...'
        cdmodel.generate(padding=0.02)  # Else defaults to 0.005 padding
        print 'ConvexDecomposition generated, saving...'
        cdmodel.save()
        print 'Finished saving'
    else:
        print 'Found ConvexDecomposition, will use loaded model.'

    print 'Setting robot...'
    cdmodel.setrobot()
    print 'Finish setrobot'

    print 'Starting visualization of the convexdecomposition model (blocking for now)'
    cdmodel.show()  #  Warning: blocking for now!

    while 1:
        pass

finally:
    RaveDestroy()
