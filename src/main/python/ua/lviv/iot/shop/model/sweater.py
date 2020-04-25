from src.main.python.ua.lviv.iot.shop.model.abstract_clothes import AbstractClothes
from src.main.python.ua.lviv.iot.shop.model.gender import Gender
from src.main.python.ua.lviv.iot.shop.model.season import Season


class Sweater(AbstractClothes):
    def __init__(self, season_name: Season, country_of_manufacture: str, brand_name: str, price_in_uah: float,
                 gender_category: Gender, material: str, color: str, size: int, item_id: int, age_group_in_years: int,
                 height_in_centimetres: int, clothes_style: str, print_type: str, knitting_type: str,
                 neck_height_in_centimetres: float) -> None:
        AbstractClothes.__init__(self, season_name, country_of_manufacture, brand_name, price_in_uah, gender_category,
                                 material, color, size, item_id, age_group_in_years, height_in_centimetres,
                                 clothes_style, print_type)
        self.knitting_type = knitting_type
        self.neck_height_in_centimetres = neck_height_in_centimetres
