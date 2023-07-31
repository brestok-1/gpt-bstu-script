import re

from docx import Document
from config import WORD_COUNT, PATH
from files import save_requests


def prepare_text(path: str) -> str:
    doc = Document(path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    text = '\n'.join(text)
    return text


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    text = text[start:]
    words = re.findall(r"\b\w+(?:[-']\w+)?\b[?.;!]*", text, re.UNICODE)[:size + 1]
    end_index = size
    for i in reversed(range(size)):
        if re.search(r'[.?;!]$', words[i]):
            end_index = i
            break
    last_word = re.escape(words[end_index])
    before_word, next_word = words[end_index - 1], words[end_index + 1]
    end_index_text = [[i.start(), i.end()] for i in re.finditer(fr'{last_word}', text)]
    for i in end_index_text:
        if before_word in text[i[0] - 30:i[0]] and next_word in text[i[1]:i[1] + 30]:
            necessary_end_index = i[1]
            break
    final_text = _create_gpt_request(text[:necessary_end_index])
    return final_text, necessary_end_index


def get_q_dict(content: str) -> dict[int:str]:
    question_dict = {}
    number = 1
    text, end_index = _get_part_text(content, 0, WORD_COUNT)
    while True:
        try:
            question_dict[number] = text.strip()
            text, index = _get_part_text(content, end_index, WORD_COUNT)
            end_index += index
            number += 1
        except IndexError:
            save_requests(question_dict)
            return question_dict


def _create_gpt_request(text: str) -> str:
    return f'Выбери 2 темы из перечисленных, которые больше всего подходят для текста\n' \
           f'Текст:\n' \
           f'{text}\n' \
           f'Темы:\n' \
           '''1. Народ
2. Метание души, поиск себя
3. Счастье
4. Смысл жизни
5. Религия вера
6. Страдания лишения, невзгоды
7. Насилие унижение
8. Война
9. Патриотизм, любовь к Родине
10. Мир
11. Любовь
12. Семья
16. Праздник
20. Выбор человека
21. Творчество
24. Болезнь
25. Вещизм (как накопление вещей)
26. Жестокость мира
27. Борьба человека
28. Возмездие
29. Преступление
30. Внутреннее состояние человека
31. Состояние природы (природа как одухотворенная красота )
35. Приспособленчество человека
36. Честность
37. Дружба
39. Одиночество человека
40. История
'''


if __name__ == '__main__':
    text = prepare_text('Shvorob.docx')
    q_dict = get_q_dict(text)
