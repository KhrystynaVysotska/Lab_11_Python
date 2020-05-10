from abc import ABC
from src.main.python.ua.lviv.iot.shop.model.abstract_goods_for_kids import AbstractGoodsForKids
from src.main.python.ua.lviv.iot.shop.model.gender import Gender
from src.main.python.ua.lviv.iot.shop.model.season import Season


class AbstractFootwear(AbstractGoodsForKids):
    def __init__(self, season_name: Season, country_of_manufacture: str, brand_name: str, price_in_uah: float,
                 gender_category: Gender, material: str, color: str, size: int, item_id: int, footwear_style: str,
                 sole_material: str, sole_height_in_milimetres: int, lining_material: str) -> None:
        AbstractGoodsForKids.__init__(self, season_name, country_of_manufacture, brand_name, price_in_uah,
                                      gender_category, material, color, size, item_id)
        self.footwear_style = footwear_style
        self.sole_material = sole_material
        self.sole_height_in_milimetres = sole_height_in_milimetres
        self.lining_material = lining_material
