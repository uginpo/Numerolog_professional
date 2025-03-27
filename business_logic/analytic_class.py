from typing import Dict, List

from loguru import logger
from business_logic.arcanes_classes import Star, Triangle
from report_storage.report_classes import Section

from text_storage.personality_dict import personality_dict
from text_storage.spirituality_dict import spirituality_dict
from text_storage.money_dict import money_dict
from text_storage.processing_dict import processing_dict
from text_storage.talents_dict import talents_dict


class StarAnalyticInfo:
    """Класс для хранения словарей аналитики страницы Звезда"""

    def __init__(self, star: Star):
        # Служебная информация
        self._star = star

        self._personality_dict = personality_dict.get(
            self._star.personality, None
        )
        self._spirituality_dict = spirituality_dict.get(
            self._star.spirituality, None
        )
        self._money_dict = money_dict.get(
            self._star.money, None)

        if not self._is_dict_correct():
            raise ValueError('В словаре(словарях) недостаточно данных')

        # Блок контента страницы аналитики
        self._personality_analytic = [
            Section(
                title='Личность',
                subtitle='Положительные черты',
                info=self._personality_dict.get('personality_positive')
            ),
            Section(
                title='Личность',
                subtitle='Отрицательные черты',
                info=self._personality_dict.get('personality_negative')
            ),
            Section(
                title='Личность',
                subtitle='Рекомендации',
                info=self._personality_dict.get('personality_recommendations')
            )
        ]

        self._spirituality_analytic = [
            Section(
                title='Духовность',
                subtitle='Программа рода:',
                info=self._spirituality_dict  # type: ignore
            )
        ]

        self._money_analytic = [
            Section(
                title='Деньги',
                subtitle='Кем Вы были в прошлой жизни?',
                info=self._money_dict.get('main_number')  # type: ignore
            ),
            Section(
                title='Деньги',
                subtitle='Профессии, которые Вам подходят:',
                info=self._money_dict.get('professions')  # type: ignore
            ),
            Section(
                title='Деньги',
                subtitle='Ваша энергия:',
                info=self._money_dict.get('energy')  # type: ignore
            ),
            Section(
                title='Деньги',
                subtitle='Ваши блоки и ограничения:',
                info=self._money_dict.get('restrictions')  # type: ignore
            ),
            Section(
                title='Деньги',
                subtitle='Траты, увеличивающие доход:',
                info=self._money_dict.get('costs')  # type: ignore
            ),
        ]

    def get_all_sections(self) -> List[Section]:
        """Возвращает контент для страницы аналитики звезды
        """
        all_sections = self._personality_analytic
        all_sections.extend(self._spirituality_analytic)
        all_sections.extend(self._money_analytic)
        return all_sections

    def _is_dict_correct(self) -> bool:
        if not self._personality_dict:
            logger.error(
                f'В словаре personality_dict отсутствует информация по ключу {self._star.personality}')

        if not self._spirituality_dict:
            logger.error(
                f'В словаре spirituality_dict отсутствует информация по ключу {self._star.spirituality}')

        if not self._money_dict:
            logger.error(
                f'В словаре money_dict отсутствует информация по ключу {self._star.money}')

        return all([self._personality_dict, self._spirituality_dict, self._money_dict])


class MoneyAnalyticInfo:
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
