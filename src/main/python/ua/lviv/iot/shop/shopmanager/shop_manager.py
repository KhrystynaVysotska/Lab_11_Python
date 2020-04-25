from typing import List
from src.main.python.ua.lviv.iot.shop.model.abstract_goods_for_kids import AbstractGoodsForKids
from src.main.python.ua.lviv.iot.shop.model.gender import Gender


class ShopManager:

    def __init__(self):
        self.list_of_goods: List[AbstractGoodsForKids] = []

    def find_goods_by_gender(self, gender: Gender) -> List[AbstractGoodsForKids]:
        list_of_founded_goods: List[AbstractGoodsForKids] = []
        for good in self.list_of_goods:
            if good.gender_category == gender:
                list_of_founded_goods.append(good)
        return list_of_founded_goods
