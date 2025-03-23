from typing import Dict

from config.settings import SCALE_PX_MM


def get_star_position() -> Dict:
    """Возвращает список координат для страницы Звезда

    Returns:
        Dict: словарь координат (mm)
    """
    scale = SCALE_PX_MM

    coordinates_px = {'header_text': (1190, 296),
                      'personality': (412, 1430),
                      'spirituality': (1190, 864),
                      'money': (1965, 1430),
                      'relationship': (1669, 2344),
                      'health': (701, 2344),
                      'pat_male_line_err': (1023, 1430),
                      'mat_male_line_err': (1370, 1430),
                      'pat_female_line_err': (1464, 1774),
                      'doom_err': (1190, 1975),
                      'mat_female_line_err': (916, 1774),
                      'mission': (1190, 1684),
                      'foot_personality': (781, 2993),
                      'foot_spirituality': (985, 2993),
                      'foot_money': (1190, 2993),
                      'foot_relationship': (1395, 2993),
                      'foot_health': (1599, 2993)}

    star_positions_mm = {key: (value[0] * scale, value[1] * scale)
                         for key, value in coordinates_px.items()}

    return star_positions_mm
