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


    def test_two_stations(self):
        stations = [self._gen_station(42, "CA"), self._gen_station(44, "CA")]
        report = build_report(stations, "CA")

        self.assertEqual(report.state, "CA")
        self.assertEqual(report.station_count, 2)
        self.assertEqual(report.maximum_elevation, 44)
        self.assertEqual(report.minimum_elevation, 42)
        self.assertEqual(report.average_elevation, 43)
        self.assertEqual(report.median_elevation, 43)

        self.assertEqual(report.median_stations, [])

        # terribly named test function; assertCountEqual checks that
        # two collections contain the same elements in any order
        self.assertCountEqual(report.lowest_stations, [stations[0]])
        self.assertCountEqual(report.highest_stations, [stations[1]])


    def test_median(self):
        stations = [self._gen_station(42, "CA"), self._gen_station(44, "CA"), self._gen_station(502, "CA")]
        report = build_report(stations, "CA")

        self.assertEqual(report.state, "CA")
        self.assertEqual(report.station_count, 3)
        self.assertEqual(report.maximum_elevation, 502)
        self.assertEqual(report.minimum_elevation, 42)
        self.assertEqual(report.average_elevation, 196)
        self.assertEqual(report.median_elevation, 44)

        # terribly named test function; assertCountEqual checks that
        # two collections contain the same elements in any order
        self.assertCountEqual(report.lowest_stations, [stations[0]])
        self.assertCountEqual(report.median_stations, [stations[1]])
        self.assertCountEqual(report.highest_stations, [stations[2]])


    def test_filtered_station(self):
        station = self._gen_station(42, "CA")
        stations = [station, self._gen_station(-1, "NV")]
        report = build_report(stations, "CA")

        self.assertEqual(report.state, "CA")
        self.assertEqual(report.station_count, 1)
        self.assertEqual(report.maximum_elevation, 42)
        self.assertEqual(report.minimum_elevation, 42)
        self.assertEqual(report.average_elevation, 42)
        self.assertEqual(report.median_elevation, 42)

        # terribly named test function; assertCountEqual checks that
        # two collections contain the same elements in any order
        self.assertCountEqual(report.median_stations, [station])
        self.assertCountEqual(report.lowest_stations, [station])
        self.assertCountEqual(report.highest_stations, [station])


    def test_empty(self):
        stations = []
        with self.assertRaises(ValueError):
            build_report(stations, "CA")


    def test_all_filtered(self):
        stations = [self._gen_station(42, "NV")]
        with self.assertRaises(ValueError):
            build_report(stations, "CA")


if __name__ == '__main__':
    unittest.main()
