from abc import ABC
from src.main.python.ua.lviv.iot.shop.model import gender, season
from src.main.python.ua.lviv.iot.shop.model.abstract_goods_for_kids import AbstractGoodsForKids


class AbstractClothes(AbstractGoodsForKids, ABC):

    def __init__(self, season_name: season, country_of_manufacture: str, brand_name: str, price_in_uah: float,
                 gender_category: gender, material: str, color: str, size: int, item_id: int, age_group_in_years: int,
                 height_in_centimetres: int, clothes_style: str, print_type: str) -> None:
        AbstractGoodsForKids.__init__(self, season_name, country_of_manufacture, brand_name, price_in_uah,
                                      gender_category, material, color, size, item_id)
        self.age_group_in_years = age_group_in_years
        self.height_in_centimetres = height_in_centimetres
        self.clothes_style = clothes_style
        self.print_type = print_type
