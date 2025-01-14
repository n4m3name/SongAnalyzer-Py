# SongAnalyzer-Py

Assignment 2 for SENG265: Software Development Methods at UVic

A Python script that analyzes Spotify song data with customizable filtering and sorting capabilities.

See the C version [here](https://github.com/n4m3name/SongAnalyzer-C)

## Features

- Filter songs by artist or year
- Sort by multiple metrics:
  - Stream count
  - Spotify playlist appearances
  - Apple Music playlist appearances
- Customizable output ordering (ascending/descending)
- Limit number of results
- Date formatting for release dates

## Usage

```bash
./song_analyzer.py [OPTIONS]
```

## Command Line Arguments

- `--data`: Input CSV file path
- `--filter`: Filter type ("ARTIST" or "YEAR")
- `--value`: Filter value
- `--order_by`: Sort column ("STREAMS", "NO_SPOTIFY_PLAYLISTS", "NO_APPLE_PLAYLISTS")
- `--order`: Sort direction ("ASC" or "DES")
- `--limit`: Maximum number of results to display

## Example Commands

```bash
# Get top 6 Dua Lipa songs by streams
./song_analyzer.py --data="data.csv" --filter="ARTIST" --value="Dua Lipa" --order_by="STREAMS" --order="ASC" --limit="6"

# Get top 20 most streamed songs
./song_analyzer.py --data="data.csv" --order_by="STREAMS" --order="DES" --limit="20"

# Get top 5 songs from 2023 by Spotify playlist appearances
./song_analyzer.py --data="data.csv" --filter="YEAR" --value="2023" --order_by="NO_SPOTIFY_PLAYLISTS" --order="DES" --limit="5"
```

## Input Format

The script expects a CSV file with the following columns:
- track_name
- artist(s)_name
- released_year
- released_month
- released_day
- streams
- in_spotify_playlists
- in_apple_playlists

## Dependencies

- Python 3.x
- pandas
- numpy
- datetime

## Author

- Original: rivera
- Modified: Evan Strasdin

Based on Spotify Songs 2023 dataset from Kaggle.
