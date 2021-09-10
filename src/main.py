import argparse
from station_report import build_report

parser = argparse.ArgumentParser(description="Analyze climate station elevation by state.")
parser.add_argument('stations', type=str, help="CSV containing station elevation data.")
parser.add_argument('--state', required=True, type=str, help="State you'd like to generate a report for.")

args = parser.parse_args()
report = build_report(args.stations, args.state)
print(report.to_json(indent=4))
