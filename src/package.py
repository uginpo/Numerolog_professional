#!/Users/user/PythonProjects/Numerolog_professional/.venv/bin/python3.13
from loguru import logger

from business_logic.arcanes_classes import Star

from input_module.clients_info import get_client_info
from data_requests.data_combiner import combine_all_data
from data_requests.fullstar_data import get_fullstar_data
from reports.pdf_creator import create_numerology_report

from statistic_service.clients_bd import clients_list


@logger.catch
def create_package_fullstar():
    """
    Главная функция программы. Выполняет следующие шаги:
    1. Получение данных клиента.
    2. Создание арканов для треугольника денег (ТД) по данным клиента.
    3. Подготовка данных для создания страницы ТД.
    4. Подготовка данных для создания страниц аналитики ТД.
    5. Объединение данных для создания страниц с настройками
       (шрифтами, координатами).
    6. Создание отчета в виде pdf файла.
    """

    # 1. Получение данных клиента

    for client in clients_list:
        client_info = get_client_info(client)

        # 2. Создание арканов для Полной Звезды по данным клиента.
        star = Star(client_info)

        # 3. Подготовка данных для создания страницы Полная Звезда.
        page_fullstar_content = get_fullstar_data(star=star)

        # 4. Подготовка данных для создания страниц ТД.
        page_fullstar_analytic = []
        union_fullstar_data = combine_all_data(
            page_fullstar_content, page_fullstar_analytic, page_name="fullstar"
        )
        # 5. Создание отчета в виде pdf файла.
        result = create_numerology_report(union_fullstar_data, pointer="fullstar")

        # Завершение работы программы
        if result:
            logger.info("Программа успешно завершила работу.")
        else:
            logger.error("Пакет не создан")


if __name__ == "__main__":
    from utils.log_utils import configure_logger

    configure_logger()
    create_package_fullstar()
