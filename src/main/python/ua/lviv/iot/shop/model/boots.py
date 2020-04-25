from src.main.python.ua.lviv.iot.shop.model import season, gender
from src.main.python.ua.lviv.iot.shop.model.abstract_footwear import AbstractFootwear


class Boots(AbstractFootwear):
    def __init__(self, season_name: season, country_of_manufacture: str, brand_name: str, price_in_uah: float,
                 gender_category: gender, material: str, color: str, size: int, item_id: int, footwear_style: str,
                 sole_material: str, sole_height_in_milimetres: int, lining_material: str,
                 insulation_material: str) -> None:
        AbstractFootwear.__init__(self, season_name, country_of_manufacture, brand_name, price_in_uah, gender_category,
                                  material, color, size, item_id, footwear_style, sole_material,
                                  sole_height_in_milimetres, lining_material)
        self.insulation_material = insulation_material
