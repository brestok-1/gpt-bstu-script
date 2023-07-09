from config import PATH
from files import save_gpt_response
from gpt import get_gpt_answers
from parse import prepare_text


def main():
    text = prepare_text(PATH)
    gpt_answers = get_gpt_answers(text)
    save_gpt_response(gpt_answers)


if __name__ == '__main__':
    main()
