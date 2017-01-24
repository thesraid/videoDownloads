#!/bin/python
# -*- coding: utf-8 -*-
# John Ó Ríordán
# 12-12-1980

import fileinput
import re
 
for line in fileinput.input():
    line = re.sub(r'\.(?=\d)', r',', line.rstrip())
    print(line)
