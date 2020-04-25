from src.main.python.ua.lviv.iot.shop.model import season, gender
from src.main.python.ua.lviv.iot.shop.model.abstract_outerwear import AbstractOuterwear


class Coat(AbstractOuterwear):
    def __init__(self, season_name: season, country_of_manufacture: str, brand_name: str, price_in_uah: float,
                 gender_category: gender, material: str, color: str, size: int, item_id: int, fastener_type: str,
                 number_of_pockets: int, lining_material: str, length_in_centimetres: float) -> None:
        AbstractOuterwear.__init__(self, season_name, country_of_manufacture, brand_name, price_in_uah, gender_category,
                                   material, color, size, item_id, fastener_type, number_of_pockets, lining_material)
        self.length_in_centimetres = length_in_centimetres
