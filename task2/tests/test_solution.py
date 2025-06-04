def test_main():
    eng_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    with open("beasts.csv", "r", newline="", encoding="UTF-8") as file:
        reader = file.read()

    for letter in eng_letters:
        if letter in reader:
            raise ValueError("В файле находится английский символ")
