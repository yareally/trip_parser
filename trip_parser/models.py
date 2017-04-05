# coding=utf-8
from datetime import datetime
from typing import Set

__author__ = 'Wes Lanning'


class Trip(object):

    def __init__(self, start_time: str, end_time: str, distance: float):
        """
        Holds data related to a single trip by a driver.
        
        :param start_time: when the trip started
        :param end_time: when it ended
        :param distance: distance driven on the trip
        """
        self.start_time = datetime.strptime(start_time, '%H:%M')
        self.end_time = datetime.strptime(end_time, '%H:%M')
        self.distance = float(distance)

    @property
    def duration(self) -> float:
        """
        Calculates the total time in as a hours for the trip
        
        :return: time in hours (with fraction of an hour) for the trip
        """
        return (self.end_time - self.start_time).total_seconds() / 3600.0

    @property
    def speed(self) -> int:
        """
        Calculates the speed for the trip.
        
        :return: speed of the trip or 0 if no duration
        """
        return 0 if self.duration == 0.0 else round(self.distance / self.duration)

    def valid_trip(self, min_speed=5, max_speed=100) -> bool:
        """
        Used to discard any trip that is under the min speed or over the max.
        
        :param min_speed: 
        :param max_speed: 
        :return: true if the trip is greater or equal to min speed and less or equal to the max.
        """
        return min_speed <= self.speed <= max_speed


class Driver(object):
    def __init__(self, name: str):
        """
        Stores the aggregated info for a driver's trips.
        
        :param name: Name of the driver who drove the trips
        """
        self.name = name
        self.trips: Set[Trip] = set()
        self._total_distance = 0.0
        self._total_duration = 0.0

    @property
    def average_speed(self) -> int:
        """
        Calculates the average speed for all trips and rounds to the nearest integer.
        
        :return: average speed of the trips or 0 if no duration
        """
        return 0 if self._total_duration == 0.0 else round(self._total_distance / self._total_duration)

    @property
    def total_distance(self) -> int:
        """
        Calculates the total distance for all trips and rounds to the nearest integer.
        
        :return: total distance rounded to nearest integer
        """
        return round(self._total_distance)

    def add_trip(self, trip: Trip) -> bool:
        """
        Adds a trip to be aggregated into the driver's stats.
        The trip will be discarded if it is under the min speed or over the max defined for the trip.
        
        :param trip: 
        :return: true if the trip was added, false if it was discarded
        """
        if trip.valid_trip():
            self.trips.add(trip)
            self._total_distance += trip.distance
            self._total_duration += trip.duration
            return True
        return False

    def __lt__(self, other) -> bool:
        """
        Defined so we can sort the trips easily in a max heap (priority queue)
        
        :param other: compare instance to this object
        :return: true if this instance is greater than the other.
        """
        return self.total_distance > other.total_distance
