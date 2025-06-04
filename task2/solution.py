import csv
import locale
import wikipediaapi
from collections import defaultdict


def main():
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent="AnimalCounterScript",
        language="ru",
        extract_format=wikipediaapi.ExtractFormat.WIKI,
    )
    page_wiki = wiki_wiki.page("Категория:Животные_по_алфавиту")
    rus_letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    letter_counter = defaultdict(int)

    # Объявить глобальные счетчик для проведения тестов
    # total_counter = 0

    for member in page_wiki.categorymembers.values():
        title = member.title.strip()
        # При сборе данных из раздела попадались эти две нижеуказанные строки
        # Добавил исключение их из добавления в счетчик
        if title and (
            title != "Категория:Знаменитые животные по алфавиту"
            and title != "Категория:Породы по алфавиту"
        ):
            # total_counter += 1
            first_letter = title[0].upper()
            if first_letter in rus_letters:
                letter_counter[first_letter] += 1

    sort_letter(letter_counter)


def sort_letter(letter_counter):
    """
    Функция сортирует полученный словарь по русскому алфавиту.
    Таким образом, буква Ё не оказывается в начале
    """

    locale.setlocale(locale.LC_COLLATE, "ru_RU.UTF-8")
    sorted_keys = sorted(letter_counter.keys(), key=locale.strxfrm)
    sorted_dict = {k: letter_counter[k] for k in sorted_keys}

    write_letter_counter(sorted_dict)


def write_letter_counter(sorted_dict):
    """
    Функция записывает результат в файл beast.csv
    """

    with open("beasts.csv", "w", newline="", encoding="UTF-8") as file:
        writer = csv.writer(file)
        for key, value in sorted_dict.items():
            writer.writerow([key, value])
    file.close()


if __name__ == "__main__":
    main()
