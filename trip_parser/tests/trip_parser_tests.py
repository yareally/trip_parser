# coding=utf-8
import unittest
from typing import List
from trip_parser.models import *
from trip_parser.parser import *

__author__ = 'Wes Lanning'


class TripParserTests(unittest.TestCase):

    def setUp(self):
        """"""
        self.driver1 = Driver('John')
        self.driver2 = Driver('Paul')
        self.driver3 = Driver('Ringo')
        self.trip1 = Trip('01:00', '2:15', 100.4)
        self.trip2 = Trip('02:00', '3:00', 4.9)
        self.trip3 = Trip('04:00', '5:00', 100.2)
        self.trip4 = Trip('07:00', '7:06', 1.9)
        self.trip5 = Trip('08:12', '8:12', 0)

    def test_parser(self):
        self.driver1.add_trip(self.trip1)
        self.driver1.add_trip(self.trip2)
        self.assertEquals(105, self.driver1.total_distance)

        self.driver2.add_trip(self.trip5)
        self.driver2.add_trip(self.trip4)
        self.assertEquals(2, self.driver2.total_distance)

        self.driver3.add_trip(self.trip5)
        self.driver3.add_trip(self.trip3)
        self.assertEquals(100, self.driver3.total_distance)

        output = output_results([self.driver1, self.driver2, self.driver3])
        print(output)
        self.assertIn('John: 105 miles @ 47 mph', output)
        self.assertIn('Paul: 2 miles @ 19 mph', output)
        self.assertIn('Ringo: 100 miles @ 100 mph', output)

    def test_trip_speed(self):
        self.assertEquals(80, self.trip1.speed)
        self.assertEquals(5, self.trip2.speed)
        self.assertEquals(100, self.trip3.speed)
        self.assertEquals(19, self.trip4.speed)
        self.assertEquals(0, self.trip5.speed)

    def test_valid_trip(self):
        self.assertTrue(self.trip1.valid_trip())
        self.assertTrue(self.trip2.valid_trip())
        self.assertTrue(self.trip3.valid_trip())
        self.assertTrue(self.trip4.valid_trip())

        self.assertFalse(self.trip5.valid_trip())

    def test_duration(self):
        self.assertEquals(1.25, self.trip1.duration)
        self.assertEquals(0.1, self.trip4.duration)
        self.assertEquals(0, self.trip5.duration)

    def test_driver_speed(self):
        self.driver1.add_trip(self.trip1)
        self.driver1.add_trip(self.trip2)
        self.assertEquals(47, self.driver1.average_speed)

        self.driver2.add_trip(self.trip5)
        self.assertEquals(0, self.driver2.average_speed)

    def test_drier_total_distance(self):
        self.driver1.add_trip(self.trip1)
        self.driver1.add_trip(self.trip2)
        self.assertEquals(105, self.driver1.total_distance)

        self.driver2.add_trip(self.trip5)
        self.driver2.add_trip(self.trip4)
        self.assertEquals(2, self.driver2.total_distance)

        self.driver3.add_trip(self.trip5)
        self.assertEquals(0, self.driver3.total_distance)

if __name__ == '__main__':
    unittest.main()
