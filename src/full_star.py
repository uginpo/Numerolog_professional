#!/Users/user/PythonProjects/Numerolog_professional/.venv/bin/python3.13
from loguru import logger
from typing import List, Dict

from business_logic.arcanes_classes import Client, Star

from input_module.clients_info import get_client_info
from data_requests.data_combiner import combine_all_data
from data_requests.fullstar_data import get_fullstar_data
from data_requests.fullstar_analityc import get_fullstar_analytic
from business_logic.analytic_class import get_triples_analytic

from reports.pdf_creator import create_numerology_report
from utils.color_utils import repr_data


# Основная функция программы
@logger.catch
def create_fullstar(client_info: Client):
    """
    Главная функция программы. Выполняет следующие шаги:
    1. Получение данных клиента.
    2. Создание арканов для полной звезды FullStar по данным клиента
       и подготовка данных для создания страницы FullStar.
    3. Объединение данных для создания страниц с настройками
       (шрифтами, координатами).
    4. Создание отчета в виде pdf файла.
    """

    # 1. Вывод данных клиента
    logger.debug(f"Имя и ДР клиента {client_info}")

    # 2. Создание арканов для FullStar по данным клиента.
    # и подготовка данных для создания страницы FullStar.
    logger.info("Создание контента страницы Fullstar")
    star = Star(client_info=client_info)

    page_fullstar_content = get_fullstar_data(star=star)
    logger.debug(f"FullStar content: {repr_data(page_fullstar_content)}")

    # 3. Подготовка данных для создания страниц аналитики звезды.
    page_of_triples: Dict | None = get_fullstar_analytic(page_fullstar_content)

    logger.debug(f"page_of_triples: {repr_data(page_of_triples)}")

    # 4. Объединение данных для создания страниц с настройками
    logger.info("Объединение данных для итогового отчета...")

    page_fullstar_analytic = get_triples_analytic(page_of_triples=page_of_triples)
    union_fullstar_data = combine_all_data(
        page_fullstar_content, page_fullstar_analytic, page_name="fullstar"
    )
    logger.debug(f"Объединенные данные {repr_data(union_fullstar_data)}")
    logger.info("Объединение данных завершено")

    # 5. Создание отчета в виде pdf файла.
    try:
        create_numerology_report(union_fullstar_data, pointer="fullstar")
    except ValueError:
        logger.error("Ошибка создания файла")


# Точка входа в программу
if __name__ == "__main__":
    from utils.log_utils import configure_logger

    client_info = get_client_info(("Julia", "23.07.1982"))

    configure_logger()
    create_fullstar(client_info)
