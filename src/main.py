import argparse
from .station import as_stations
from .station_report import build_report, StationReport


def _parse_args():
    parser = argparse.ArgumentParser(prog="analyze-elevation", description="Analyze climate station elevation by state.")
    parser.add_argument('stations', type=str, help="CSV containing station elevation data.", metavar="STATIONS_FILE")
    parser.add_argument('--state', required=True, type=str, help="State you'd like to generate a report for.")

    return parser.parse_args()


def _create_report(station_file: str, state: str) -> StationReport:
    with open(station_file) as station_content:
        stations = as_stations(station_content)
        return build_report(stations, state)


def run():
    args = _parse_args()
    try:
        report = _create_report(args.stations, args.state)
        report.dump()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    run()
