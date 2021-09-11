from src.station import Station
import unittest
import random
from src.station import Station
from src.station_report import build_report

class TestStationReport(unittest.TestCase):

    def _gen_station(self, elevation: float, state: str) -> Station:
        uid = random.randint(0, 100000)
        return Station(
            uid=uid,
            state=state,
            name=f"nicename-{elevation}-{state}-{uid}",
            ll=f"[{random.uniform(-90, 90)}, {random.uniform(-180, 180)}]",
            elev=elevation
        )


    def test_one_station(self):
        station = [self._gen_station(42, "CA")]
        report = build_report(station, "CA")

        self.assertEqual(report.state, "CA")
        self.assertEqual(report.station_count, 1)
        self.assertEqual(report.maximum_elevation, 42)
        self.assertEqual(report.minimum_elevation, 42)
        self.assertEqual(report.average_elevation, 42)
        self.assertEqual(report.median_elevation, 42)

        # terribly named test function; assertCountEqual checks that
        # two collections contain the same elements in any order
        self.assertCountEqual(report.median_stations, station)
        self.assertCountEqual(report.lowest_stations, station)
        self.assertCountEqual(report.highest_stations, station)

if __name__ == '__main__':
    unittest.main()