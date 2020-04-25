from typing import List
from src.main.python.ua.lviv.iot.shop.model.abstract_goods_for_kids import AbstractGoodsForKids
from src.main.python.ua.lviv.iot.shop.model.gender import Gender
from src.main.python.ua.lviv.iot.shop.model.season import Season
from src.main.python.ua.lviv.iot.shop.model.sort_type import SortType
from doctest import testmod

from src.main.python.ua.lviv.iot.shop.model.sweater import Sweater


class ShopManagerUtils:

    @staticmethod
    def sort_goods_by_price(goods: List[AbstractGoodsForKids], sort_type: SortType) -> List[AbstractGoodsForKids]:
        """
        Test of correct sorting list by price ascending
        >>> sorted_list_by_price_ascending = ShopManagerUtils.sort_goods_by_price(list_of_goods_to_test, SortType.ASCENDING)
        >>> [good.price_in_uah for good in sorted_list_by_price_ascending]
        [340, 450, 490, 560]

        Test of correct sorting list by price descending
        >>> sorted_list_by_price_descending = ShopManagerUtils.sort_goods_by_price(list_of_goods_to_test, SortType.DESCENDING)
        >>> [good.price_in_uah for good in sorted_list_by_price_descending]
        [560, 490, 450, 340]
        """
        sorted_list_of_goods_by_price: List[AbstractGoodsForKids] = []
        if sort_type == SortType.ASCENDING:
            sorted_list_of_goods_by_price = sorted(goods, key=lambda good: good.price_in_uah)
        elif sort_type == SortType.DESCENDING:
            sorted_list_of_goods_by_price = sorted(goods, key=lambda good: good.price_in_uah, reverse=True)
        return sorted_list_of_goods_by_price

    @staticmethod
    def sort_goods_by_size(goods: List[AbstractGoodsForKids], sort_type: SortType) -> List[AbstractGoodsForKids]:
        """
        Test of correct sorting list by size ascending
        >>> sorted_list_by_size_ascending = ShopManagerUtils.sort_goods_by_size(list_of_goods_to_test, SortType.ASCENDING)
        >>> [good.size for good in sorted_list_by_size_ascending]
        [35, 36, 38, 39]

        Test of correct sorting list by size descending
        >>> sorted_list_by_size_descending = ShopManagerUtils.sort_goods_by_size(list_of_goods_to_test, SortType.DESCENDING)
        >>> [good.size for good in sorted_list_by_size_descending]
        [39, 38, 36, 35]
        """
        sorted_list_of_goods_by_size: List[AbstractGoodsForKids] = []
        if sort_type == SortType.ASCENDING:
            sorted_list_of_goods_by_size = sorted(goods, key=lambda good: good.size)
        elif sort_type == SortType.DESCENDING:
            sorted_list_of_goods_by_size = sorted(goods, key=lambda good: good.size, reverse=True)
        return sorted_list_of_goods_by_size


if __name__ == '__main__':
    first_good: AbstractGoodsForKids = Sweater(Season.AUTUMN, "Chinese", "Chicco", 450, Gender.BOY, "cotton", "blue",
                                               38, 1543, 6,
                                               116, "casual", "none", "machine tool", 0.0)
    second_good: AbstractGoodsForKids = Sweater(Season.WINTER, "Ukraine", "TopHat", 560, Gender.GIRL, "knitwear",
                                                "white", 36, 3654,
                                                12, 156, "casual", "flower", "hand knitting", 3)
    third_good: AbstractGoodsForKids = Sweater(Season.AUTUMN, "Sweden", "H&M", 340, Gender.BOY, "cotton", "haki", 39,
                                               3434, 7, 122,
                                               "casual", "dragon", "machine tool", 0.0)
    forth_good: AbstractGoodsForKids = Sweater(Season.AUTUMN, "Ukraine", "Flash", 490, Gender.GIRL, "wool", "grey", 35,
                                               1234, 9, 134,
                                               "casual", "rombus", "hand knitting", 4)
    list_of_goods_to_test: List[AbstractGoodsForKids] = [first_good, second_good, third_good, forth_good]
    testmod(name='sort_goods_by_price', verbose=True)
    testmod(name='sort_goods_by_size', verbose=True)
