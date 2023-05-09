from dataclasses import dataclass


@dataclass
class Speaker:
    name: str
    image: str
    role: str
    profile_url: str
    pronoun: str = ''
