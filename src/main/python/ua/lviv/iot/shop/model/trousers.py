from src.main.python.ua.lviv.iot.shop.model import season, gender
from src.main.python.ua.lviv.iot.shop.model.abstract_clothes import AbstractClothes


class Trousers(AbstractClothes):
    def __init__(self, season_name: season, country_of_manufacture: str, brand_name: str, price_in_uah: float,
                 gender_category: gender, material: str, color: str, size: int, item_id: int, age_group_in_years: int,
                 height_in_centimetres: int, clothes_style: str, print_type: str, waist_height_in_centimetres: float,
                 tailoring_type: str) -> None:
        AbstractClothes.__init__(self, season_name, country_of_manufacture, brand_name, price_in_uah, gender_category,
                                 material, color, size, item_id, age_group_in_years, height_in_centimetres,
                                 clothes_style, print_type)
        self.waist_height_in_centimetres = waist_height_in_centimetres
        self.tailoring_type = tailoring_type
