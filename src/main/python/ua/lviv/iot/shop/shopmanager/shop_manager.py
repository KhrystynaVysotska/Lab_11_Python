from typing import List
from src.main.python.ua.lviv.iot.shop.model.abstract_goods_for_kids import AbstractGoodsForKids
from src.main.python.ua.lviv.iot.shop.model.gender import Gender
from src.main.python.ua.lviv.iot.shop.model.season import Season
from src.main.python.ua.lviv.iot.shop.model.sweater import Sweater
from doctest import testmod


class ShopManager:

    def __init__(self):
        self.list_of_goods: List[AbstractGoodsForKids] = []

    def find_goods_by_gender(self, gender: Gender) -> List[AbstractGoodsForKids]:
        """
        Test of correct founding goods for girls in the list
        >>> shop_manager = ShopManager()
        >>> shop_manager.list_of_goods.append(Sweater(Season.AUTUMN, "Chinese", "Chicco", 450, Gender.BOY, "cotton",
        ...                                         "blue", 38, 1543, 6,116, "casual", "none", "machine tool", 0.0))
        >>> shop_manager.list_of_goods.append(Sweater(Season.WINTER, "Ukraine", "TopHat", 560, Gender.GIRL, "knitwear",
        ...                                             "white", 36, 3654,12, 156, "casual", "flower", "hand knitting", 3))
        >>> shop_manager.list_of_goods.append(Sweater(Season.AUTUMN, "Sweden", "H&M", 340, Gender.BOY, "cotton", "haki",
        ...                                                39,3434, 7, 122,"casual", "dragon", "machine tool", 0.0))
        >>> shop_manager.list_of_goods.append(Sweater(Season.AUTUMN, "Ukraine", "Flash", 490, Gender.GIRL, "wool", "grey", 35,
        ...                                               1234, 9, 134,"casual", "rombus", "hand knitting", 4))
        >>> list_of_founded_goods_by_gender = shop_manager.find_goods_by_gender(Gender.GIRL)
        >>> len(list_of_founded_goods_by_gender)
        2
        """
        list_of_founded_goods: List[AbstractGoodsForKids] = []
        for good in self.list_of_goods:
            if good.gender_category == gender:
                list_of_founded_goods.append(good)
        return list_of_founded_goods

    def find_goods_by_season(self, season: Season) -> List[AbstractGoodsForKids]:
        """
        Test of correct founding goods for autumn in the list
        >>> shop_manager = ShopManager()
        >>> shop_manager.list_of_goods.append(Sweater(Season.AUTUMN, "Chinese", "Chicco", 450, Gender.BOY, "cotton",
        ...                                         "blue", 38, 1543, 6,116, "casual", "none", "machine tool", 0.0))
        >>> shop_manager.list_of_goods.append(Sweater(Season.WINTER, "Ukraine", "TopHat", 560, Gender.GIRL, "knitwear",
        ...                                             "white", 36, 3654,12, 156, "casual", "flower", "hand knitting", 3))
        >>> shop_manager.list_of_goods.append(Sweater(Season.AUTUMN, "Sweden", "H&M", 340, Gender.BOY, "cotton", "haki",
        ...                                                39,3434, 7, 122,"casual", "dragon", "machine tool", 0.0))
        >>> shop_manager.list_of_goods.append(Sweater(Season.AUTUMN, "Ukraine", "Flash", 490, Gender.GIRL, "wool", "grey", 35,
        ...                                               1234, 9, 134,"casual", "rombus", "hand knitting", 4))
        >>> list_of_founded_goods_by_season = shop_manager.find_goods_by_season(Season.AUTUMN)
        >>> len(list_of_founded_goods_by_season)
        3
        """
        list_of_founded_goods: List[AbstractGoodsForKids] = []
        for good in self.list_of_goods:
            if good.season_name == season:
                list_of_founded_goods.append(good)
        return list_of_founded_goods


if __name__ == '__main__':
    testmod(verbose=True)
