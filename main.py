#!/usr/bin/env python
# coding=utf-8
from typing import List
from trip_parser.models import *
from trip_parser.parser import *

__author__ = 'Wes Lanning'

""" Reads from stdin or an input file of drivers and their trips. 
    Outputs aggregated data for each driver's trips.
    
    assumptions:
    - there will be input from either stdin or a file
    - if not stdin, file exists (exception is not handled, since you can't do much without input anyways)
    - if stdin and no input, press ctrl+d to quit
    - using Python 3.6+
"""


if __name__ == '__main__':
    drivers: List[Driver] = list(parse_input().values())
    output_results(drivers)
