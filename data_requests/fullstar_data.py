from business_logic.arcanes_classes import Client, Star, Triangle

from typing import Dict, ChainMap
from collections import defaultdict


def get_fullstar_data(star: Star) -> Dict:
    """Возвращает контент для создания страницы
    Полная Звезда FullStar

    Args:
        star (Star): Данные star для клиента

    Returns:
        Dict: словарь FullStar
    """
    star_data: Dict = defaultdict(str)
    star_data = {key: value for key, value in star.get_all_content().items()}

    triangles_data = defaultdict(str)
    for triangle in ['personality', 'spirituality', 'money', 'relationship', 'health']:
        triangle_dict = Triangle(
            star=star,
            pointer=triangle).get_inv_triangle()
        for key, value in triangle_dict.items():
            triangles_data[f'{triangle}_{key}'] = value

    return star_data | triangles_data
