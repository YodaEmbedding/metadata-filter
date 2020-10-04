# metadata-filter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Cleaner metadata (e.g. artist, album, track titles) for scrobbling.

## Install

```python
pip install metadata-filter
```

## Usage

```python
from metadata_filter import *

artist = "Iron Maiden"
album = "Powerslave (2015 Remaster)"
track = "Aces High - 2015 Remaster"

rules = (
    REMASTERED_FILTER_RULES
    + SUFFIX_FILTER_RULES
    + VERSION_FILTER_RULES
    + ORIGIN_FILTER_RULES
    + FEATURE_FILTER_RULES
    + CLEAN_EXPLICIT_FILTER_RULES
    + LIVE_FILTER_RULES
    + TRIM_WHITESPACE_FILTER_RULES
)

track = apply_filters(rules, track)
album = apply_filters(rules, album)

print(f"{artist} - {album} - {track}")

# Prints:
# Iron Maiden - Powerslave - Aces High
```
