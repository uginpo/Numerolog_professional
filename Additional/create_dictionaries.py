import random
import json


def generate_lorem_ipsum(num_sentences):
    lorem_text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                  "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
                  "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                  "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
                  "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    sentences = lorem_text.split('. ')
    result = '. '.join(random.choices(sentences, k=num_sentences)) + '.'
    return result


def create_number_info(number):
    return {
        number: {
            'personality_positive': [generate_lorem_ipsum(4)],
            'personality_negative': [generate_lorem_ipsum(3)],
            'personality_recommendations': [generate_lorem_ipsum(3)]
        }
    }


def create_number_info_res(number):
    return {
        number: [generate_lorem_ipsum(4)],
    }


# Создаем общий словарь для чисел от 10 до 20
combined_dict = {}
for num in range(10, 23):
    combined_dict.update(create_number_info(num))

# Выводим словарь в файл в формате JSON
file_name = "number_info.json"
with open(file_name, "w", encoding="utf-8") as file:
    json.dump(combined_dict, file, ensure_ascii=False, indent=4)

print(f"Словарь успешно записан в файл {file_name}")
