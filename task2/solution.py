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
    rus_dict = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    letter_counter = defaultdict(int)
    total_counter = 0
    rus_letter_counter = 0
    for member in page_wiki.categorymembers.values():
        title = member.title.strip()
        if title and (
            title != "Категория:Знаменитые животные по алфавиту"
            and title != "Категория:Породы по алфавиту"
        ):
            total_counter += 1
            first_letter = title[0].upper()
            if first_letter in rus_dict:
                rus_letter_counter += 1
                letter_counter[first_letter] += 1

    locale.setlocale(locale.LC_COLLATE, "ru_RU.UTF-8")
    sorted_keys = sorted(letter_counter.keys(), key=locale.strxfrm)
    sorted_dict = {k: letter_counter[k] for k in sorted_keys}

    write_letter_counter(sorted_dict)


def write_letter_counter(sorted_dict):
    with open("beasts.csv", "w", newline="", encoding="UTF-8") as file:
        writer = csv.writer(file)
        for key, value in sorted_dict.items():
            writer.writerow([key, value])


if __name__ == "__main__":
    main()
