"""
Build the different distribution packages for the OpenDeck.
"""

import os
from typing import Sequence
from zipfile import ZipFile

SUITS = {
    "allsuits": [
        "acorns",
        "bells",
        "clubs",
        "cups",
        "diamonds",
        "hearts",
        "leaves",
        "spades",
        "stars",
        "swords",
    ],
    "trad4": [
        "clubs",
        "diamonds",
        "hearts",
        "spades",
    ],
    "new6": [
        "acorns",
        "bells",
        "cups",
        "leaves",
        "stars",
        "swords",
    ],
}

VALUES = {
    "allvalues": [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "A",
        "F",
        "J",
        "K",
        "Q",
        "S",
        "W",
    ],
    "tradvalues": [
        "A",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
    ],
    "numbers": [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
    ],
    "sheepshead": [
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
        "A",
    ],
}

JOKERS = {
    "0j": [],
    "2j": ["1", "3"],
    "3j": ["1", "2", "3"],
}


def build_zip(
    filename: str, suits: Sequence[str], values: Sequence[str], jokers: Sequence[str]
):
    """
    Create a zip file containing the images for the given deck configuration.
    """
    with ZipFile(f"dist/{filename}", "w") as zfile:
        for suit in suits:
            for value in values:
                card = f"{suit}{value}.jpg"
                zfile.write(f"images/{card}", card)
        for joker in jokers:
            card = f"joker{joker}.jpg"
            zfile.write(f"images/{card}", card)


def main():
    """
    Build all of the distributions.
    """
    os.makedirs("./dist", exist_ok=True)
    for suits_name, suits in SUITS.items():
        for values_name, values in VALUES.items():
            for jokers_name, jokers in JOKERS.items():
                filename = f"opendeck_{suits_name}_{values_name}_{jokers_name}.zip"
                build_zip(filename, suits, values, jokers)


if __name__ == "__main__":
    main()
