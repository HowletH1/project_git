text = input('строка: ')


def upper():
"""
    эта функция преобразовывает нижний регистр текста
    в верхний
    :return:
    текст заглавными буквами
    """
    if text == text.lower():
        return text.upper()


print(upper())
