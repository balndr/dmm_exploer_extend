# -*- coding:utf-8 -*-
import sys
import os
import bottle

dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dirpath)
os.chdir(dirpath)

import index

application = bottle.default_app()
