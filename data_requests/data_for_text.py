from typing import List, Dict, Any

from business_logic.arcanes_classes import Star, Pifagor, Triangle
from business_logic.analytic_class import StarAnalyticDict, MoneyAnalyticDict


def get_star_analytic(star: Star) -> List:
    """Создает структуру для заполнения страницы с аналитикой по странице star
    Args:
        star (Star): Класс Star, заполненный значениями арканов

    Returns:
        data_lst: список словарей для заполнения страницы аналитики
    """

    for current_dict, title in zip(StarAnalyticDict(star=star).get_star_list(), ['Личность', 'Духовность', 'Деньги']):

        match title:
            case 'Личность':

                person_list: List = [
                    {
                        'title': 'Личность',
                        'subtitle': 'Положительные черты:',
                        'info': current_dict["personality_positive"]
                    },
                    {
                        'title': 'Личность',
                        'subtitle': 'Отрицательные черты:',
                        'info': current_dict["personality_negative"]
                    },
                    {
                        'title': 'Личность',
                        'subtitle': 'Рекомендации:',
                        'info': current_dict["personality_recommendations"]
                    }
                ]

            case 'Духовность':

                spirit_list: List = [
                    {
                        'title': 'Духовность',
                        'subtitle':   'Программа рода:',
                        'info': current_dict
                    }
                ]

            case 'Деньги':

                money_list: List = [
                    {
                        'title': 'Деньги',
                        'subtitle': 'Кем Вы были в прошлой жизни?',
                        'info': current_dict.get("main_number", "Отсутствуют данные в словаре Деньги для такого аркана")
                    },
                    {
                        'title': 'Деньги',
                        'subtitle': 'Профессии, которые Вам подходят:',
                        'info': current_dict["professions"]
                    },
                    {
                        'title': 'Деньги',
                        'subtitle': 'Ваша энергия:',
                        'info': current_dict["energy"]
                    },
                    {
                        'title': 'Деньги',
                        'subtitle': 'Ваши блоки и ограничения:',
                        'info': current_dict["restrictions"]
                    },
                    {
                        'title': 'Деньги',
                        'subtitle': 'Траты, увеличивающие доход:',
                        'info': current_dict["costs"]
                    }
                ]

    return [*person_list, *spirit_list, *money_list]


def get_money_analytic(money: Triangle) -> List:
    """Создает структуру для заполнения страницы с аналитикой по странице star
    Args:
        money (Trianlge): Класс Triangle, заполненный значениями арканов

    Returns:
        data_lst: список словарей для заполнения страницы аналитики
    """

    for current_dict, title in zip(MoneyAnalyticDict(money=money), ['Деньги', 'Проработка', 'Ваши скрытые таланты']):

        match title:
            case 'Деньги':

                mon_dict: Dict | Any = current_dict.get(money.vertex)
                money_list: List = [
                    {
                        'title': 'Деньги',
                        'subtitle': 'Кем Вы были в прошлой жизни?',
                        'info': mon_dict.get("main_number", "Отсутствуют данные в словаре Деньги для такого аркана")
                    },
                    {
                        'title': 'Деньги',
                        'subtitle': 'Профессии, которые Вам подходят:',
                        'info': mon_dict["professions"]
                    },
                    {
                        'title': 'Деньги',
                        'subtitle': 'Ваша энергия:',
                        'info': mon_dict["energy"]
                    },
                    {
                        'title': 'Деньги',
                        'subtitle': 'Ваши блоки и ограничения:',
                        'info': mon_dict["restrictions"]
                    },
                    {
                        'title': 'Деньги',
                        'subtitle': 'Траты, увеличивающие доход:',
                        'info': mon_dict["costs"]
                    }
                ]
            case 'Проработка':

                my_dict: Dict | Any = current_dict.get(star.personality)
                person_list: List = [
                    {
                        'title': 'Личность',
                        'subtitle': 'Положительные черты:',
                        'info': my_dict["personality_positive"]
                    },
                    {
                        'title': 'Личность',
                        'subtitle': 'Отрицательные черты:',
                        'info': my_dict["personality_negative"]
                    },
                    {
                        'title': 'Личность',
                        'subtitle': 'Рекомендации:',
                        'info': my_dict["personality_recommendations"]
                    }
                ]

            case 'Духовность':

                spirit_list: List = [
                    {
                        'title': 'Духовность',
                        'subtitle':   'Программа рода:',
                        'info': current_dict.get(star.spirituality)
                    }
                ]

    return [*person_list, *spirit_list, *money_list]
