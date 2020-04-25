from src.main.python.ua.lviv.iot.shop.model.abstract_footwear import AbstractFootwear
from src.main.python.ua.lviv.iot.shop.model.gender import Gender
from src.main.python.ua.lviv.iot.shop.model.season import Season


class Shoes(AbstractFootwear):
    def __init__(self, season_name: Season, country_of_manufacture: str, brand_name: str, price_in_uah: float,
                 gender_category: Gender, material: str, color: str, size: int, item_id: int, footwear_style: str,
                 sole_material: str, sole_height_in_milimetres: int, lining_material: str, shoes_type: str,
                 ankle_height_in_centimetres: float) -> None:
        AbstractFootwear.__init__(self, season_name, country_of_manufacture, brand_name, price_in_uah, gender_category,
                                  material, color, size, item_id, footwear_style, sole_material,
                                  sole_height_in_milimetres, lining_material)
        self.shoes_type = shoes_type
        self.ankle_height_in_centimetres = ankle_height_in_centimetres

