from enum import Enum


class Season(str, Enum):
    WINTER: str = "WINTER"
    SPRING: str = "SPRING"
    AUTUMN: str = "AUTUMN"
    SUMMER: str = "SUMMER"