# -*- Coding: utf-8 -*-
# Author: Yu

import os

BASE_DIR = '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
date_path = os.path.join(BASE_DIR, 'data')

school_file = os.path.join(date_path, 'school')
