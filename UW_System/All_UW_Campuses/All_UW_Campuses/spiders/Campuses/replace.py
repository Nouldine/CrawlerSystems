#!/usr/bin/env python3

import fileinput

with fileinput.FileInput('MadisonAreaTechCollege.csv', inplace = True, backup='.bak' ) as file: 
    for line in file:
        
        print(line.replace('UW Branch Campus', '9999'))
