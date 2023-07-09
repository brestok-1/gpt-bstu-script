from docx import Document
from config import WORD_COUNT


def prepare_text(path: str) -> str:
    doc = Document(str)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    text = '\n'.join(text)
    return text


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    text = text[start:]
    words = re.findall(r'\b[А-Яа-яЁё]+\b[?.!]*', text)[:size + 1]
    end_index = size
    for i in reversed(range(size)):
        if re.search(r'[.?!]$', words[i]):
            end_index = i
            break
    last_word = words[end_index]
    before_word, next_word = words[end_index - 1], words[end_index + 1]
    end_index_text = [[i.start(), i.end()] for i in re.finditer(fr'{last_word}', text)]
    necessary_end_index = None
    for i in end_index_text:
        if re.search(fr'{before_word}', text[i[0] - 30:i[0]]) and re.search(fr'{next_word}', text[i[1]:i[1] + 30]):
            necessary_end_index = i[1]
    final_text = _create_request_gpt(text[:necessary_end_index])
    return final_text, len(final_text)


def _create_request_gpt(text: str) -> str:
    return f'Какие две темы из перечисленных ниже наиболее всего подходят для текста и почему\n' \
           f'Текст:\n' \
           f'{text}\n' \
           f'Темы:\n' \
           '''1. Народ (значимость простого народа образ его жизни ход мыслей )
2. Метание души, поиск себя
3. Счастье
4. Смысл жизни
5. Религия вера
6. Страдания лишения, невзгоды
7. Насилие унижение
8. Война
9. Патриотизм, любовь к Родине
10. Мир
11. Любовь (страсть и страдание как составляющие любви, поиск духовной близости и понимания)
12. Семья
13. Научный проект
14. Предсказание будущего
15. Описание прошлого
16. Праздник
17. Океан
18. Космос
19. Техническое устройство
20. Выбор человека
21. Творчество
22. Что такое добро
23. Что есть зло
24. Болезнь
25. Вещизм (как накопление вещей)
26. Жестокость мира
27. Борьба человека
28. Возмездие
29. Преступление
30. Внутреннее состояние человека
31. Состояние природы (природа как одухотворенная красота )
32. Прогресс (как развитие общества и человека)
33. Разложение верхов общества (власти)
34. Подавление личности
35. Приспособленчество человека
36. Честность
37. Дружба
38. Судьба поколения (отрицание существующей действительности, бездуховность общества)
39. Одиночество человека (мотив непонятости, усталости и безысходности)
40. История (обращение к отечественной истории и поиск идеалов в прошлом)
41. Избранность (особенность) художника (судьба поэта-писателя-художника и его творений)'''


def get_q_dict(content: str) -> dict[int:str]:
    book_dict = {}
    number = 1
    text, end_index = _get_part_text(content, 0, WORD_COUNT)
    while True:
        try:
            book_dict[number] = text.strip()
            text, index = _get_part_text(content, end_index, WORD_COUNT)
            end_index += index
            number += 1
        except IndexError:
            return book_dict
