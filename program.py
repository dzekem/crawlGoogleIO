from dataclasses import dataclass
from typing import List

from speaker import Speaker


@dataclass
class Program:
    profile_image: str
    title: str
    description: str
    short_description: str
    tags: str
    url: str
    speakers: List[Speaker]
    following_session: str = ''
