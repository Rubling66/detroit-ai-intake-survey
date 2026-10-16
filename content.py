"""Content contract for a stored snapshot.

The record a caller can mean is SnapshotEntry.
This module does not open files and does not list the notes in the tree.
"""

from typing import Final, Tuple, TypedDict


class SnapshotEntry(TypedDict):
    kind: str
    entry: str


KIND: Final[str] = "snapshot"
ENTRY: Final[str] = "README.md"


def snapshot_entry() -> SnapshotEntry:
    return {"kind": KIND, "entry": ENTRY}


CONTENT: Final[Tuple[str, ...]] = ("SnapshotEntry",)
