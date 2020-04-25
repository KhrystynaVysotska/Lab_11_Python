from abc import ABC
from src.main.python.ua.lviv.iot.shop.model import season, gender


class AbstractGoodsForKids(ABC):

    def __init__(self, season_name: season, country_of_manufacture: str, brand_name: str, price_in_uah: float,
                 gender_category: gender, material: str, color: str, size: int, item_id: int) -> None:
        self.season_name = season_name
        self.country_of_manufacture = country_of_manufacture
        self.brand_name = brand_name
        self.price_in_uah = price_in_uah
        self.gender_category = gender_category
        self.material = material
        self.color = color
        self.size = size
        self.item_id = item_id
