from dataclasses import dataclass


@dataclass
class Speaker:
    name: str
    image: str
    role: str
    profile_url: str
    pronoun: str = ''

    """
    Each Speaker has a unique profile. We can use this as the identifier for uniqueness of a speaker.
    We could have used something like the speaker name or their image but we assume here that each speaker has a 
    """

    def __hash__(self):
        return hash(self.profile_url)
