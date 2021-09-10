import argparse
from station_report import build_report

def _parse_args():
    parser = argparse.ArgumentParser(prog="analyze-elevation", description="Analyze climate station elevation by state.")
    parser.add_argument('stations', type=str, help="CSV containing station elevation data.", metavar="STATIONS_FILE")
    parser.add_argument('--state', required=True, type=str, help="State you'd like to generate a report for.")

    return parser.parse_args()

def _write_report(station_file: str, state: str):
    report = build_report(station_file, state)
    report.dump()

def run():
    args = _parse_args()
    _write_report(args.stations, args.state)

run()