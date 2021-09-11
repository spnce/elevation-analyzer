# Elevation Analyzer

Tool for reading and analyzing climate station elevations.

## Usage

`./analyze-elevation [-h] --state STATE STATIONS_FILE`

- `STATE` two-letter state abbreviation
- `STATIONS_FILE` csv file with columns:
  - `uid` (int): The station's unique identifier.
  - `state` (str): The state where the station is located.
  - `name` (str): A descriptive name of the station.
  - `ll` (str): The station's latitude & longitude. Ex: "[42, -120]"
  - `elev` (float): The elevation of the station.

Places a file called "elevation_report_STATE.json" in the local directory.

## Testing

`./run-tests`

## Requirements

- python3
- pipenv
