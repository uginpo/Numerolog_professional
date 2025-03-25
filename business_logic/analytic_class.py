from typing import Dict, List

from loguru import logger
from business_logic.arcanes_classes import Star, Triangle

from text_storage.personality_dict import personality_dict
from text_storage.spirituality_dict import spirituality_dict
from text_storage.money_dict import money_dict
from text_storage.processing_dict import processing_dict
from text_storage.talents_dict import talents_dict


class StarAnalyticDict:
    """Класс для хранения словарей аналитики страницы Звезда"""

    def __init__(self, star: Star):
        # Служебная информация
        self._star = star
        self._personality_dict = personality_dict
        self._spirituality_dict = spirituality_dict
        self._money_dict = money_dict

        # Блок
        self.title = 'Личность'

    def get_star_list(self) -> List:
        """
        Возвращает список словарей для создания страницы
        Returns:
            List: Список словарей
        """
        # Проверка на полноту информации словарей БД
        # В каждом словаре должна быть информация по своему аркану
        self.pers_dict = self.personality_dict.get(
            self.star.personality, None)

        self.spir_dict = self.spirituality_dict.get(
            self.star.spirituality, None)

        self.mon_dict = self.money_dict.get(
            self.star.money, None)

        if not self.pers_dict:
            logger.error(
                f'В словаре personality_dict отсутствует информация по ключу {self.star.personality}')

        if not self.spir_dict:
            logger.error(
                f'В словаре spirituality_dict отсутствует информация по ключу {self.star.spirituality}')

        if not self.mon_dict:
            logger.error(
                f'В словаре money_dict отсутствует информация по ключу {self.star.money}')

        if any([self.pers_dict, self.spir_dict, self.mon_dict]):
            raise ValueError('В словаре(словарях) недостаточно данных')

        # Возврат только необходимой информации для заполнения страницы аналитики
        return [self.pers_dict, self.spir_dict, self.mon_dict]


class MoneyAnalyticDict:
    """Класс для хранения словарей аналитики страницы ДТ
    """

    def __init__(self, money: Triangle) -> None:
        self.money = money
        self.processing_dict = processing_dict
        self.talents_dict = talents_dict
        self.money_dict = money_dict

    def get_money_list(self) -> List:
        """
        Возвращает список словарей для создания страницы
        Returns:
            List: Список словарей c необходимой информацией
        """

        self.mon_dict = self.money_dict.get(
            self.money.vertex, None)

        if not self.mon_dict:
            logger.error(
                f'В словаре money_dict отсутствует информация по ключу {self.money.vertex}')
            raise ValueError('В словаре недостаточно данных')

        money_list = [self.mon_dict]

        if self.money.inv_vertex != self.money.vertex:
            self.proc_dict = self.processing_dict.get(
                self.money.inv_vertex, None)

            if not self.proc_dict:
                logger.error(
                    f'В словаре processing_dict отсутствует информация по ключу {self.money.inv_vertex}')
                raise ValueError('В словаре недостаточно данных')

            money_list.append(self.proc_dict)

        for number in [self.money.mat_vertex, self.money.pat_vertex, self.money.inv_mat_vertex, self.money.inv_pat_vertex]:

            if number not in [self.money.vertex, self.money.inv_vertex]:

                self.tal_dict = self.talents_dict.get(number, None)
                if not self.tal_dict:
                    logger.error(
                        f'В словаре talents_dict отсутствует информация по ключу {number}')
                    raise ValueError('В словаре недостаточно данных')
                else:
                    money_list.append({str(number): self.tal_dict})

        return money_list
