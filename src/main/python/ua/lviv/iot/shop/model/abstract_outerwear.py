from abc import ABC
from src.main.python.ua.lviv.iot.shop.model.abstract_goods_for_kids import AbstractGoodsForKids
from src.main.python.ua.lviv.iot.shop.model.gender import Gender
from src.main.python.ua.lviv.iot.shop.model.season import Season


class AbstractOuterwear(AbstractGoodsForKids, ABC):
    def __init__(self, season_name: Season, country_of_manufacture: str, brand_name: str, price_in_uah: float,
                 gender_category: Gender, material: str, color: str, size: int, item_id: int, fastener_type: str,
                 number_of_pockets: int, lining_material: str) -> None:
        AbstractGoodsForKids.__init__(self, season_name, country_of_manufacture, brand_name, price_in_uah,
                                      gender_category, material, color, size, item_id)
        self.fastener_type = fastener_type
        self.number_of_pockets = number_of_pockets
        self.lining_material = lining_material
