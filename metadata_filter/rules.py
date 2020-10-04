"""
Filter rules are an array that contains replace rules.

Each rule is an object that contains 'source' and 'target' properties.
'source' property is a string or RegEx object which is replaced by
'target' property value.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class FilterRule:
    source: str
    target: str


YOUTUBE_TRACK_FILTER_RULES: List[FilterRule] = [
    # Trim whitespaces (beginning)
    FilterRule(source=r"/^\s+/", target=""),
    # Trim whitespaces (end)
    FilterRule(source=r"/\s+$/", target=""),
    # **NEW**
    FilterRule(source=r"/\*+\s?\S+\s?\*+$/", target=""),
    # [whatever]
    FilterRule(source=r"/\[[^\]]+\]/", target=""),
    # (whatever version)
    FilterRule(source=r"/\([^)]*version\)$/i", target=""),
    # video extensions
    FilterRule(source=r"/\.(avi|wmv|mpg|mpeg|flv)$/i", target=""),
    # (LYRICs VIDEO)
    FilterRule(source=r"/\(.*lyrics?\s*(video)?\)/i", target=""),
    # (Official Track Stream)
    FilterRule(source=r"/\((of+icial\s*)?(track\s*)?stream\)/i", target=""),
    # (official)? (music)? video
    FilterRule(source=r"/\((of+icial\s*)?(music\s*)?video\)/i", target=""),
    # (official)? (music)? audio
    FilterRule(source=r"/\((of+icial\s*)?(music\s*)?audio\)/i", target=""),
    # (ALBUM TRACK)
    FilterRule(source=r"/(ALBUM TRACK\s*)?(album track\s*)/i", target=""),
    # (Cover Art)
    FilterRule(source=r"/(COVER ART\s*)?(Cover Art\s*)/i", target=""),
    # (official)
    FilterRule(source=r"/\(\s*of+icial\s*\)/i", target=""),
    # (1999)
    FilterRule(source=r"/\(\s*[0-9]{4}\s*\)/i", target=""),
    # HD (HQ)
    FilterRule(source=r"/(HD|HQ)\s*$/", target=""),
    # video clip officiel or video clip official
    FilterRule(source=r"/(vid[\u00E9e]o)?\s?clip\sof+ici[ae]l/i", target=""),
    # offizielles
    FilterRule(source=r"/of+iziel+es\s*video/i", target=""),
    # video clip
    FilterRule(source=r"/vid[\u00E9e]o\s?clip/i", target=""),
    # clip
    FilterRule(source=r"/\sclip/i", target=""),
    # Full Album
    FilterRule(source=r"/full\s*album/i", target=""),
    # (live)
    FilterRule(source=r"/\(live.*?\)$/i", target=""),
    # | something
    FilterRule(source=r"/\|.*$/i", target=""),
    # Artist - The new "Track title" featuring someone
    FilterRule(source=r'/^(|.*\s)"(.{5,})"(\s.*|)$/', target=r"\2"),
    # 'Track title'
    FilterRule(source=r"/^(|.*\s)'(.{5,})'(\s.*|)$/", target=r"\2"),
    # (*01/01/1999*)
    FilterRule(
        source=r"/\(.*[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{2,4}.*\)/i", target=""
    ),
    # Sub Español
    FilterRule(source=r"/sub\s*español/i", target=""),
    # (Letra/Lyrics)
    FilterRule(source=r"/\s\(Letra\/Lyrics\)/i", target=""),
    # (Letra)
    FilterRule(source=r"/\s\(Letra\)/i", target=""),
    # (En vivo)
    FilterRule(source=r"/\s\(En\svivo\)/i", target=""),
    # Sub Español
    FilterRule(source=r"/sub\s*español/i", target=""),
]

TRIM_SYMBOLS_FILTER_RULES: List[FilterRule] = [
    # Leftovers after e.g. (official video)
    FilterRule(source=r"/\(+\s*\)+/", target=""),
    # trim starting white chars and dash
    FilterRule(source=r'/^[/,:;~-\s"]+/', target=""),
    # trim trailing white chars and dash
    FilterRule(source=r'/[/,:;~-\s"]+$/', target=""),
]

REMASTERED_FILTER_RULES: List[FilterRule] = [
    # Here Comes The Sun - Remastered
    FilterRule(source=r"/-\sRemastered$/", target=""),
    # Hey Jude - Remastered 2015
    FilterRule(source=r"/-\sRemastered\s\d+$/", target=""),
    # Let It Be (Remastered 2009)
    # Red Rain (Remaster 2012)
    FilterRule(source=r"/\(Remaster(ed)?\s\d+\)$/", target=""),
    # Pigs On The Wing (Part One) [2011 - Remaster]
    FilterRule(source=r"/\[\d+\s-\sRemaster\]$/", target=""),
    # Comfortably Numb (2011 - Remaster)
    # Dancing Days (2012 Remaster)
    FilterRule(source=r"/\(\d+(\s-)?\sRemaster\)$/", target=""),
    # Outside The Wall - 2011 - Remaster
    # China Grove - 2006 Remaster
    FilterRule(source=r"/-\s\d+(\s-)?\sRemaster$/", target=""),
    # Learning To Fly - 2001 Digital Remaster
    FilterRule(source=r"/-\s\d+\s.+?\sRemaster$/", target=""),
    # Your Possible Pasts - 2011 Remastered Version
    FilterRule(source=r"/-\s\d+\sRemastered Version$/", target=""),
    # Roll Over Beethoven (Live / Remastered)
    FilterRule(source=r"/\(Live\s\/\sRemastered\)$/i", target=""),
    # Ticket To Ride - Live / Remastered
    FilterRule(source=r"/-\sLive\s\/\sRemastered$/", target=""),
    # Mothership (Remastered)
    # How The West Was Won [Remastered]
    FilterRule(source=r"/[([]Remaster(ed)?[)\]]$/", target=""),
    # A Well Respected Man (2014 Remastered Version)
    # A Well Respected Man [2014 Remastered Version]
    FilterRule(source=r"/[([]\d{4} Re[Mm]astered Version[)\]]$/", target=""),
    # She Was Hot (2009 Re-Mastered Digital Version)
    # She Was Hot (2009 Remastered Digital Version)
    FilterRule(
        source=r"/[([]\d{4} Re-?[Mm]astered Digital Version[)\]]$/", target=""
    ),
    # In The Court Of The Crimson King (Expanded & Remastered Original Album Mix)
    FilterRule(source=r"/\([^\(]*Remaster[^\)]*\)$/", target=""),
]

LIVE_FILTER_RULES: List[FilterRule] = [
    # Track - Live
    FilterRule(source=r"/-\sLive?$/", target=""),
    # Track - Live at
    FilterRule(source=r"/-\sLive\s.+?$/", target=""),
    # (Live) or [Live]
    FilterRule(source=r"/\s[([]Live[)\]]/i", target=""),
]

CLEAN_EXPLICIT_FILTER_RULES: List[FilterRule] = [
    # (Explicit) or [Explicit]
    FilterRule(source=r"/\s[([]Explicit[)\]]/i", target=""),
    # (Clean) or [Clean]
    FilterRule(source=r"/\s[([]Clean[)\]]/i", target=""),
]

FEATURE_FILTER_RULES: List[FilterRule] = [
    # [Feat. Artist] or (Feat. Artist)
    FilterRule(source=r"/\s[([]feat. .+[)\]]/i", target=""),
]

NORMALIZE_FEATURE_FILTER_RULES: List[FilterRule] = [
    # [Feat. Artist] or (Feat. Artist) -> Feat. Artist
    FilterRule(source=r"/\s[([](feat. .+)[)\]]/i", target=r" \1"),
]

VERSION_FILTER_RULES: List[FilterRule] = [
    # Love Will Come To You (Album Version)
    FilterRule(source=r"/[([]Album Version[)\]]$/", target=""),
    # I Melt With You (Rerecorded)
    # When I Need You [Re-Recorded]
    FilterRule(source=r"/[([]Re-?recorded[)\]]$/", target=""),
    # Your Cheatin' Heart (Single Version)
    FilterRule(source=r"/[([]Single Version[)\]]$/", target=""),
    # All Over Now (Edit)
    FilterRule(source=r"/[([]Edit[)\]]$/", target=""),
    # (I Can't Get No) Satisfaction - Mono Version
    FilterRule(source=r"/-\sMono Version$/", target=""),
    # Ruby Tuesday - Stereo Version
    FilterRule(source=r"/-\sStereo Version$/", target=""),
    # Pure McCartney (Deluxe Edition)
    FilterRule(source=r"/\(Deluxe Edition\)$/", target=""),
    # 6 Foot 7 Foot (Explicit Version)
    FilterRule(source=r"/[([]Explicit Version[)\]]/i", target=""),
    # Sgt. Pepper's Lonely Hearts Club Band (Super Deluxe Edition)
    FilterRule(
        source=r"/\([^\(]*(Deluxe|Edition|Version)[^\)]*\)$/",
        target="",
    ),
    # Blowin' The Blues Away - Rudy Van Gelder Edition
    FilterRule(source=r"/-\s.*(Deluxe|Edition|Version)$/", target=""),
]

SUFFIX_FILTER_RULES: List[FilterRule] = [
    # "- X Remix" -> "(X Remix)" and similar
    FilterRule(
        source=r"/-\s(.+?)\s((Re)?mix|edit|dub|mix|vip|version)$/i",
        target=r"(\1 \2)",
    ),
    # "- X Remix" -> "(X Remix)" and similar
    FilterRule(source=r"/-\s(Remix|VIP)$/i", target=r"(\1)"),
]

ORIGIN_FILTER_RULES: List[FilterRule] = [
    # For The First Time In Forever (From "Frozen")
    FilterRule(source=r"/\s\([fF]rom [^\)]+\)/i", target=""),
    # Vuelie - From "Frozen"/Score
    FilterRule(source=r"/-\sFrom\s[^-]+$/i", target=""),
]

TRIM_WHITESPACE_FILTER_RULES: List[FilterRule] = [
    # Trim whitespaces (beginning)
    FilterRule(source=r"/^\s+/", target=""),
    # Trim whitespaces (end)
    FilterRule(source=r"/\s+$/", target=""),
]

__all__ = [
    "FilterRule",
    "CLEAN_EXPLICIT_FILTER_RULES",
    "FEATURE_FILTER_RULES",
    "LIVE_FILTER_RULES",
    "NORMALIZE_FEATURE_FILTER_RULES",
    "ORIGIN_FILTER_RULES",
    "REMASTERED_FILTER_RULES",
    "SUFFIX_FILTER_RULES",
    "TRIM_SYMBOLS_FILTER_RULES",
    "TRIM_WHITESPACE_FILTER_RULES",
    "VERSION_FILTER_RULES",
    "YOUTUBE_TRACK_FILTER_RULES",
]
