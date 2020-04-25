from typing import List
from src.main.python.ua.lviv.iot.shop.model.abstract_goods_for_kids import AbstractGoodsForKids
from src.main.python.ua.lviv.iot.shop.model.sort_type import SortType


class ShopManagerUtils:

    @staticmethod
    def sort_goods_by_price(goods: List[AbstractGoodsForKids], sort_type: SortType) -> List[AbstractGoodsForKids]:
        sorted_list_of_goods_by_price: List[AbstractGoodsForKids] = []
        if sort_type == SortType.ASCENDING:
            sorted_list_of_goods_by_price = sorted(goods, key=lambda good: good.price_in_uah)
        elif sort_type == SortType.DESCENDING:
            sorted_list_of_goods_by_price = sorted(goods, key=lambda good: good.price_in_uah, reverse=True)
        return sorted_list_of_goods_by_price

    @staticmethod
    def sort_goods_by_size(goods: List[AbstractGoodsForKids], sort_type: SortType) -> List[AbstractGoodsForKids]:
        sorted_list_of_goods_by_size: List[AbstractGoodsForKids] = []
        if sort_type == SortType.ASCENDING:
            sorted_list_of_goods_by_size = sorted(goods, key=lambda good: good.size)
        elif sort_type == SortType.DESCENDING:
            sorted_list_of_goods_by_size = sorted(goods, key=lambda good: good.size, reverse=True)
        return sorted_list_of_goods_by_size
    