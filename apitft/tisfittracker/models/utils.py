from enum import Enum


class Difficulty(Enum):
    TRES_FACILE = "Très facile"
    FACILE = "Facile"
    MOYEN = "Moyen"
    DIFFICILE = "Difficile"
    TRES_DIFFICILE = "Très difficile"


class Type(Enum):
    PUSH = "Push"
    PULL = "Pull"
    LEGS = "Legs"
