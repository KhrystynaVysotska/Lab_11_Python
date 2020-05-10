from src.main.python.ua.lviv.iot.shop.model.abstract_accessories import AbstractAccessories
from src.main.python.ua.lviv.iot.shop.model.gender import Gender
from src.main.python.ua.lviv.iot.shop.model.season import Season


class Backpack(AbstractAccessories):
    def __init__(self, season_name: Season, country_of_manufacture: str, brand_name: str, price_in_uah: float,
                 gender_category: Gender, material: str, color: str, size: int, item_id: int, accessories_type: str,
                 print_type: str, length_in_centimetres: float, width_in_centimetres: float,
                 height_in_centimetres: float, weight_in_kilograms: float,
                 max_capacity_in_litres: float, number_of_compartments: int) -> None:
        AbstractAccessories.__init__(self, season_name, country_of_manufacture, brand_name, price_in_uah,
                                     gender_category, material, color, size, item_id, accessories_type,
                                     print_type)
        self.length_in_centimetres = length_in_centimetres
        self.width_in_centimetres = width_in_centimetres
        self.height_in_centimetres = height_in_centimetres
        self.weight_in_kilograms = weight_in_kilograms
        self.max_capacity_in_litres = max_capacity_in_litres
        self.number_of_compartments = number_of_compartments
