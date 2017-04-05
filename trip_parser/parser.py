# coding=utf-8
import fileinput
import heapq

from typing import List, Dict
from trip_parser.models import *

__author__ = 'Wes Lanning'


def parse_input() -> Dict[str, Driver]:
    """
    Reads driver/trip input from stdin or a file and
    then parses that info into usable objects

    :return: a dictionary mapping drivers to their trips
    """
    lines: List[str] = [line.rstrip('\n') for line in fileinput.input()]
    drivers: Dict[str, Driver] = {}

    for line in lines:
        cmd, *tail = line.split(' ')
        driver_name, *data = tail

        try:
            if driver_name in drivers and data:
                drivers[driver_name].add_trip(Trip(*data))
            else:
                drivers[driver_name] = Driver(driver_name)
        except Exception as ex:
            print(ex)

    return drivers


def output_results(drivers: List[Driver], units_of_measure=('miles', 'mph')) -> str:
    """
    Dumps aggregated results for each driver to stdout

    :param drivers: list of all drivers we parsed from input and their stats
    :param units_of_measure: appends the given unit measure type
    """
    heapq.heapify(drivers)
    output = ''

    for driver in drivers:
        output += f'{driver.name}: {driver.total_distance} {units_of_measure[0]}'
        output += f' @ {driver.average_speed} {units_of_measure[1]}' if driver.average_speed else ''
        output += '\n'

    return output
