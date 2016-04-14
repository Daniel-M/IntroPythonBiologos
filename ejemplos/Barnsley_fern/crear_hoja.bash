#!/bin/bash
python3 fern.py | sed 's/\[//g;s/\]//g;s/\,/  /g' > datos-1.dat 
python3 fern_2.py | sed 's/\[//g;s/\]//g;s/\,/  /g' > datos-2.dat 
