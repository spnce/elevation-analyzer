import argparse

parser = argparse.ArgumentParser(description="Analyze climate station elevation by state.")
parser.add_argument('stations', type=str, help="CSV containing station elevation data.")
parser.add_argument('--state', type=str, help="State you'd like to generate a report for.")

args = parser.parse_args()