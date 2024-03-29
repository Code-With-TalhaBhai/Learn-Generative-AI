from model import Creature

_creature = [
    Creature(
        name="horse",
        country="africa",
        area="blue city",
        description="Rare horse found in europe",
        aka='hr'
    ),Creature(
        name="octupus",
        country="sea",
        area="lower sea",
        description="A fish with many hands",
        aka='ocu'
    )
]



def get_creatures():
    return _creature