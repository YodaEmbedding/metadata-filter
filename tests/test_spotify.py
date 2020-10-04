from typing import List, Tuple

import pytest

from metadata_filter import *
from metadata_filter.rules import *

# fmt: off
album_tests: List[Tuple[str, str]] = [
    (
        "Awake",
        "Awake",
    ),
    (
        "Frozen",
        "Frozen (Original Motion Picture Soundtrack / Deluxe Edition)",
    ),
    (
        "Frozen 2",
        "Frozen 2 (Original Motion Picture Soundtrack/Deluxe Edition)",
    ),
    (
        "In The Court Of The Crimson King",
        "In The Court Of The Crimson King "
        "(Expanded & Remastered Original Album Mix)",
    ),
    (
        "Moanin'",
        "Moanin' (The Rudy Van Gelder Edition)",
    ),
    (
        "Rock In Rio",
        "Rock In Rio [Live]",
    ),
    (
        "Sgt. Pepper's Lonely Hearts Club Band",
        "Sgt. Pepper's Lonely Hearts Club Band (Super Deluxe Edition)",
    ),
]

track_tests: List[Tuple[str, str]] = [
    (
        "21st Century Schizoid Man",
        "21st Century Schizoid Man [Bonus Track] - Radio Version",
    ),
    (
        "A Man A City",
        "A Man A City [Bonus Track] - Live At the Fillmore West",
    ),
    (
        "For the First Time in Forever",
        'For the First Time in Forever (From "Frozen"/Soundtrack Version)',
    ),
    (
        "Home - Outtake",
        "Home - Outtake",
    ),
    (
        "I Talk To The Wind",
        "I Talk To The Wind [Bonus Track] - Duo Version",
    ),
    (
        "Layla",
        "Layla - Acoustic; Live at MTV Unplugged, Bray Film Studios, Windsor, "
        "England, UK, 1/16/1992; 2013 Remaster",
    ),
    (
        "Moanin' (Alternate Take)",
        "Moanin' (Alternate Take)",
    ),
    (
        "Moonchild",
        'Moonchild - Including "The Dream" and "The Illusion"',
    ),
    (
        "The Bard's Song - In the Forest",
        "The Bard's Song - In the Forest"
    ),
    (
        "The Chill Of Death(Recitation by Charles Mingus)",
        "The Chill Of Death(Recitation by Charles Mingus)",
    ),
    (
        "The Court Of The Crimson King",
        "The Court Of The Crimson King - Including "
        '"The Return of the Fire Witch" and "The Dance of the Puppets"',
    ),
    (
        "The Fellowship Reunited",
        "The Fellowship Reunited "
        "(Feat. Sir James Galway, Viggo Mortensen And Renée Fleming)",
    ),
    (
        "Vuelie",
        'Vuelie - From "Frozen"/Score',
    ),
]
# fmt: on

# fmt: off
custom_album_tests: List[Tuple[str, str]] = [
    (
        "Frozen (Original Motion Picture Soundtrack)",
        "Frozen (Original Motion Picture Soundtrack)",
    ),
    (
        "Frozen 2 (Original Motion Picture Soundtrack/Deluxe Edition)",
        "Frozen 2 (Original Motion Picture Soundtrack/Deluxe Edition)",
    ),
    (
        "The Lord of the Rings: Return of the King - the Complete Recordings",
        "The Lord of the Rings - The Return of the King - "
        "The Complete Recordings (Limited Edition)",
    ),
]

custom_track_tests: List[Tuple[str, str]] = [
    (
        "A Change Of Seasons",
        "A Change Of Seasons - The Crimson Sunrise / Innocence / Carpe Diem / "
        "The Darkest Of Winters / Another World / The Inevitable Summer / "
        "The Crimson Sunset",
    ),
    (
        "Better Git It in Your Soul",
        "Better Get Hit In Your Soul - Instrumental",
    ),
]
# fmt: on

tests = album_tests + track_tests


@pytest.mark.parametrize("title_expected,title_input", tests)
def test_filters(title_input, title_expected):
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
    title_actual = apply_filters(rules, title_input)
    assert title_actual == title_expected
