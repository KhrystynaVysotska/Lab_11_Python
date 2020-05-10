from src.main.python.ua.lviv.iot.shop.model.abstract_accessories import AbstractAccessories
from src.main.python.ua.lviv.iot.shop.model.gender import Gender
from src.main.python.ua.lviv.iot.shop.model.season import Season


class Gloves(AbstractAccessories):
    def __init__(self, season_name: Season, country_of_manufacture: str, brand_name: str, price_in_uah: float,
                 gender_category: Gender, material: str, color: str, size: int, item_id: int, accessories_type: str,
                 print_type: str, fingers_number: int) -> None:
        AbstractAccessories.__init__(self, season_name, country_of_manufacture, brand_name, price_in_uah,
                                     gender_category, material, color, size, item_id, accessories_type,
                                     print_type)
        self.fingers_number = fingers_number
